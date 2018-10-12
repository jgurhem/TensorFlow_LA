#!/usr/bin/python

import tensorflow as tf
import printutils as pu
import mvop
import sys

if len(sys.argv) != 5:
    print "Wrong number of arguments !"
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

for i in range(N):
    b[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i))
    pu.outData("b.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j))
        pu.outData("a.dat", A[i,j], matsize, matsize, i, j)


sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

l = mvop.powerIT(sess, A, b, N, matsize, itmax, epsilon)

print "l", sess.run(l)

for i in range(N):
    pu.outData("r.dat", b[i], matsize, 1, i, 0)

merged = tf.summary.merge_all()
