#!/bin/sh -e

N=3
nb=4

python ../applications/tf_dgeaxpxmv.py $N $nb
check_results -op dgeaxpxmv -A a.dat -V b.dat -R r.dat -print -b $N -s $nb
