#!/bin/sh
set -e

N=3
nb=4

python ../applications/tf_dgeaxpxmv.py $N $nb
check_results -ff coo -op dgeaxpxmv -A a.dat -V b.dat -R r.dat -b $N -s $nb
