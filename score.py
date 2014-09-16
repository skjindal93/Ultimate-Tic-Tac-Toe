sum=0
import sys
with open('submissions/'+sys.argv[1] + ".score",'r') as scorefile:
	for line in scorefile:
		sum = sum + int(line)
		
with open('submissions/'+sys.argv[1] + ".score",'w') as scfile:
	scfile.write(str(sum))