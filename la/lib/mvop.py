import tensorflow as tf
import numpy as np
import math


def printv(sess, name, b, N, matsize):
    s = name
    for i in range(N):
        bv = sess.run(b[i])
        for j in range(matsize):
            s += " {:.6f}".format(bv[j, 0])
    print s


def dotVect(sess, a, b, N, matsize):
    s = 0
    for i in range(N):
        s += tf.matmul(a[i], b[i], transpose_a=True)
    return tf.reshape(s, []);


def normalize(sess, b, N, matsize):
    norm = tf.sqrt(dotVect(sess, b, b, N, matsize))
    x = {}
    for i in range(N):
        x[i] = tf.scalar_mul(1/norm, b[i])
    return x


def pmv(A, x, N, matsize):
    b = {}
    for i in range(N):
        b[i] = tf.constant(0.0, shape=[matsize, 1])
        for j in range(N):
            b[i] = tf.add(b[i], tf.matmul(A[i,j], x[j], name="mul{}{}".format(i, j)))
    return b


def powerIT(sess, A, x, N, matsize, itmax, epsilon):
    i = 0
    l = 0.0
    la = 1.0
    e = tf.constant(epsilon)
    while i < itmax and sess.run(tf.greater(tf.abs(l - la), e)):
        la = l
        b = normalize(sess, x, N, matsize)
        x = pmv(A, b, N, matsize)
        l = dotVect(sess, b, x, N, matsize)
        i += 1
    return l
