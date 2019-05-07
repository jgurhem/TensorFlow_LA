#!/bin/sh
set -e

N=3
nb=4

python ../applications/tf_mm.py $N $nb
check_results -ff coo -A a.dat -B b.dat -C c.dat -b $N -s $nb -op mm
