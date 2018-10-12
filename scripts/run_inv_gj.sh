#!/bin/sh -e

N=3
nb=4

python ../applications/tf_inv_gj.py $N $nb
check_results -op invgj -A a.dat -B inv.dat -b $N -s $nb -print
