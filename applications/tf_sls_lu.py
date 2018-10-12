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
pu.init("lu.dat")

for i in range(N):
    b[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i), name="b{}".format(i))
    pu.outData("b.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))
        pu.outData("a.dat", A[i,j], matsize, matsize, i, j)


sess = tf.Session()
init = tf.global_variables_initializer()


for k in range(N):
    inv[k] = tf.matrix_inverse(A[k, k])
    for i in range(k + 1, N):
        A[i,k] = tf.matmul(A[i,k], inv[k])
        for j in range(k + 1, N):
            A[i,j] = A[i,j] - tf.matmul(A[i,k], A[k,j])


for i in range(N - 1):
    for j in range(i + 1, N):
        b[j] = b[j] - tf.matmul(A[j, i], b[i])
    

for k in range(N - 1, -1, -1):
    b[k] = tf.matrix_solve(A[k, k], b[k])
    for i in range(0, k):
        b[i] = b[i] - tf.matmul(A[i, k], b[k])
    

for i in range(N):
    pu.outData("r.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        pu.outData("lu.dat", A[i,j], matsize, matsize, i, j)

sess.run(init)
