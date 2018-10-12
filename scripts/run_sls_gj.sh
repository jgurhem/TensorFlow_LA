#!/bin/sh -e

N=3
nb=4

python ../applications/tf_sls_gj.py $N $nb
check_results -A a.dat -V b.dat -R r.dat -op slsg -b $N -s $nb
