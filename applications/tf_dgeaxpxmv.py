#!/usr/bin/python

import tensorflow as tf
import lib.printutils as pu
import sys

if len(sys.argv) != 3:
    print "Wrong number of arguments !"
    sys.exit(1)

N = int(sys.argv[1])
matsize = int(sys.argv[2])

A = {}
b = {}
r = {}
x = {}

pu.init("a.dat")
pu.init("b.dat")
pu.init("r.dat")

sess = tf.Session()

for i in range(N):
    b[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i), name="b{}".format(i))
    x[i] = tf.Variable(tf.random_uniform([matsize, 1], seed = N * N + i), name="b{}".format(i))
    for j in range(N):
        A[i,j] = tf.Variable(tf.random_uniform([matsize, matsize], seed = i * N + j), name="A{}{}".format(i, j))


init = tf.global_variables_initializer()
sess.run(init)

for i in range(N):
    pu.outData(sess, "b.dat", b[i], matsize, 1, i, 0)
    for j in range(N):
        pu.outData(sess, "a.dat", A[i,j], matsize, matsize, i, j)

for i in range(N):
    r[i] = b[i]
    for j in range(N):
        r[i] = tf.assign_add(r[i], tf.matmul(A[i,j], b[i], name="mul{}{}".format(i, j)), True, "add{}{}".format(i, j))

for i in range(N):
    x[i] = tf.assign(x[i], r[i])

for i in range(N):
    for j in range(N):
        x[i] = tf.assign_add(x[i], tf.matmul(A[i,j], r[i], name="mul2{}{}".format(i, j)), True, "add2{}{}".format(i, j))

for i in range(N):
    pu.outData(sess, "r.dat", x[i], matsize, 1, i, 0)

