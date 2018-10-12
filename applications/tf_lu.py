#!/usr/bin/python

import tensorflow as tf
import printutils as pu
import sys

if len(sys.argv) != 3:
    print "Wrong number of arguments !"
    sys.exit(1)

N = int(sys.argv[1])
matsize = int(sys.argv[2])

A = {}
inv = {}

pu.init("a.dat")
pu.init("lu.dat")

for i in range(N):
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))
        pu.outData("a.dat", A[i,j], matsize, matsize, i, j)


sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for k in range(N):
    inv[k] = tf.matrix_inverse(A[k, k])
    for i in range(k + 1, N):
        A[i,k] = tf.matmul(A[i,k], inv[k])
        for j in range(k + 1, N):
            A[i,j] = A[i,j] - tf.matmul(A[i,k], A[k,j])

for i in range(N):
    for j in range(N):
        pu.outData("lu.dat", A[i,j], matsize, matsize, i, j)
