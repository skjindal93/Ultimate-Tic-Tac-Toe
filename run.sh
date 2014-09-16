#!/bin/bash
sub="submissions/"
sco=$2.score
w=$2.win
l=$2.lost
p=$2.py
e=$2.error
rm $sub$e
rm $sub$sco
rm lock
pidfile=$2.pid
while true; do
	if [ ! -f lock ] ; then
		touch lock
		break
	else 
		sleep 1
	fi
done

for i in {1..10} 
do
	cat $1 >> tmp.txt
	string=$(grep "import" tmp.txt)
	echo $string
	if [ "$string" != "" ] ; then rm tmp.txt; echo "You have used import" >> $sub$e; exit 0; fi
	echo $1
	sed -i "s/^/\t/" tmp.txt
	cat part1.py tmp.txt enter.txt part2.py >> tmp.py
	echo "start"
	echo $$ > $sub$pidfile
	timeout 120 python tmp.py $2 2> $sub$e
	echo "end"
	#if [ $? -eq  0 ] ; then echo "Done"; else python failhandle.py error.tmp $2 ; fi

	rm tmp.txt
	rm tmp.py
	#rm error.tmp
done
python score.py $2
chmod 750 $sub$w $sub$sco $sub$l $sub$p
rm $sub$pidfile
rm lock