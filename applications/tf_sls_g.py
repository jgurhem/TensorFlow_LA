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
b = {}
inv = {}

pu.init("a.dat")
pu.init("b.dat")
pu.init("r.dat")

for i in range(N):
    b[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i), name="b{}".format(i))
    pu.outData("b.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))
        pu.outData("a.dat", A[i,j], matsize, matsize, i, j)


sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for k in range(N):
    inv[k] = tf.matrix_inverse(A[k,k])
    b[k] = tf.matmul(inv[k], b[k])
    for i in range(k + 1, N):
        A[k,i] = tf.matmul(inv[k], A[k,i])
    for i in range(k + 1, N):
        b[i] = b[i] - tf.matmul(A[i,k], b[k])
        for j in range(k + 1, N):
            A[i,j] = A[i,j] - tf.matmul(A[i,k], A[k,j])

for k in range(1, N):
    for i in range(N - k):
        b[i] = b[i] - tf.matmul(A[i, N - k], b[N - k])

for i in range(N):
    pu.outData("r.dat", b[i], matsize, 1, i, 0)

merged = tf.summary.merge_all()
