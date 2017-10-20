#!/bin/bash
declare -a var
var=( 2 3 4 5 8 10 15 20 30 35 40 50 60 70 80 90 100 ) # Values in M

size() {
	mb=$1
	echo $(expr $mb \* 1024)
}

for i in "${var[@]}"
# for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
do 
	#dd if=/dev/zero of=${var[$i]}  bs=${var[$i]} count=1
	dd if=/dev/urandom of=${i}MB bs=$(size $i) count=1024
done
exit 0
