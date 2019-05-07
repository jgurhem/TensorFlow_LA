#!/usr/bin/python

import tensorflow as tf
import lib.printutils as pu
import sys
import numpy as np

if len(sys.argv) != 3:
    print("Wrong number of arguments !")
    sys.exit(1)

N = int(sys.argv[1])
matsize = int(sys.argv[2])

A = {}
B = {}
C = {}

pu.init("a.dat")
pu.init("b.dat")
pu.init("c.dat")
sess = tf.Session()

for i in range(N):
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))
        B[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = (N + i + 1) * N + j), name="B{}{}".format(i, j))
        C[i,j] = tf.Variable(tf.constant(0, shape=[matsize, matsize], dtype=np.float32), name="B{}{}".format(i, j))

init = tf.global_variables_initializer()
sess.run(init)

for i in range(N):
    for j in range(N):
        pu.outData(sess, "a.dat", A[i,j], matsize, matsize, i, j)
        pu.outData(sess, "b.dat", B[i,j], matsize, matsize, i, j)

for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] = C[i,j] + tf.matmul(A[i,k], B[k,j])

for i in range(N):
    for j in range(N):
        pu.outData(sess, "c.dat", C[i,j], matsize, matsize, i, j)
