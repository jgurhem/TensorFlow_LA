#!/bin/sh -e

N=3
nb=4

python ../applications/tf_lu.py $N $nb
check_results -A a.dat -B lu.dat -b $N -s $nb -op blu
