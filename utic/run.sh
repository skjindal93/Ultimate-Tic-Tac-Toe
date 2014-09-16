#!/bin/bash
echo "Abhay"
while true; do
	if [ ! -f lock ] ; then
		touch lock
		break
	else 
		sleep 1
	fi
done

for i in {1..1} 
do
	echo "for loop"
	cat $1 >> tmp.txt
	sed -i "s/^/\t/" tmp.txt
	cat part1.py tmp.txt part2.py >> tmp.py
	echo "start"
	python tmp.py --id=$2 2> error.tmp
	echo "end"
	#if [ $? -eq  0 ] ; then echo "Done"; else python failhandle.py error.tmp $2 ; fi

	rm tmp.txt
	rm tmp.py
	rm error.tmp
done
	
rm lock