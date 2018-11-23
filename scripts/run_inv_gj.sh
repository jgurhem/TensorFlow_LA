#!/bin/sh
set -e

N=3
nb=4

python ../applications/tf_inv_gj.py $N $nb
check_results -ff coo -op invgj -A a.dat -B inv.dat -b $N -s $nb
