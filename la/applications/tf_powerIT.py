#!/usr/bin/python

import tensorflow as tf
import lib.printutils as pu
import lib.mvop as mvop
import sys

if len(sys.argv) != 5:
    print("Wrong number of arguments !")
    sys.exit(1)

N = int(sys.argv[1])
matsize = int(sys.argv[2])
itmax = int(sys.argv[3])
epsilon = float(sys.argv[4])

A = {}
b = {}
inv = {}

pu.init("a.dat")
pu.init("b.dat")
pu.init("r.dat")
sess = tf.Session()

for i in range(N):
    b[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i))
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j))

init = tf.global_variables_initializer()
sess.run(init)

for i in range(N):
    pu.outData(sess, "b.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        pu.outData(sess, "a.dat", A[i,j], matsize, matsize, i, j)

l = mvop.powerIT(sess, A, b, N, matsize, itmax, epsilon)

print("l1 =", sess.run(l))

for i in range(N):
    pu.outData(sess, "r.dat", b[i], matsize, 1, i, 0)

merged = tf.summary.merge_all()
