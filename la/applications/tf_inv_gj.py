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
B = {}
inv = {}
tmp = {}

pu.init("a.dat")
pu.init("inv.dat")

sess = tf.Session()

for i in range(N):
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))
        if i==j:
            B[i,i] = tf.Variable(tf.eye(matsize))
        else:
            B[i,j] = tf.Variable(tf.zeros([matsize, matsize]))
        tmp[i,j] = tf.Variable(tf.zeros([matsize, matsize]))

init = tf.global_variables_initializer()
sess.run(init)

for i in range(N):
    for j in range(N):
        pu.outData(sess, "a.dat", A[i,j], matsize, matsize, i, j)

for k in range(N):
    inv[k] = tf.matrix_inverse(A[k, k])
    for j in range(N):
        A[k,j] = tf.matmul(inv[k], A[k,j])
        B[k,j] = tf.matmul(inv[k], B[k,j])
    for i in range(k):
        tmp[i,k] = tf.tile(A[i,k], tf.ones([2], tf.int32))
        for j in range(N):
            A[i,j] = A[i,j] - tf.matmul(tmp[i,k], A[k,j])
            B[i,j] = B[i,j] - tf.matmul(tmp[i,k], B[k,j])
    for i in range(k+1, N):
        tmp[i,k] = tf.tile(A[i,k], tf.ones([2], tf.int32))
        for j in range(N):
            A[i,j] = A[i,j] - tf.matmul(tmp[i,k], A[k,j])
            B[i,j] = B[i,j] - tf.matmul(tmp[i,k], B[k,j])

for i in range(N):
    for j in range(N):
        pu.outData(sess, "inv.dat", B[i,j], matsize, matsize, i, j)
