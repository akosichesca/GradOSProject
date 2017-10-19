#!/bin/bash
declare -a var
var=( 2000 3000 4000 5000 8000 10000 15000 20000 30000 35000 40000 50000 60000 70000 80000 90000 10000 )

for i in "${var[@]}"
# for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
do 
#	dd if=/dev/zero of=${var[$i]}  bs=${var[$i]} count=1
	dd if=/dev/zero of=$i bs=$i count=1
done
exit 0
