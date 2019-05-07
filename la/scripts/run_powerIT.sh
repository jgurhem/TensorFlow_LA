#!/bin/sh
set -e

N=3
nb=4
itmax=15

python ../applications/tf_powerIT.py $N $nb $itmax 0.000001
check_results -ff coo -p 0.000001 -b $N -s $nb -it $itmax -op powerIt -A a.dat -V b.dat
