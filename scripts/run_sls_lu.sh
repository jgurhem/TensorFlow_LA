#!/bin/sh -e

N=4
nb=3

python ../applications/tf_sls_lu.py $N $nb
check_results -A a.dat -V b.dat -R r.dat -op slsg -b $N -s $nb
