import MySQLdb
import os
import sys

db = MySQLdb.connect(host="localhost",user="trystiit_uttt",passwd="uttt@vindy2014",db="trystiit_ultimate")
cursor = db.cursor()

errormsg = ""
with open(os.getcwd() + "/"+ sys.argv[1]) as errfile:
	for line in errfile:
		errormsg += line
		cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(sys.argv[2]),0,0,errormsg,"Error",0))		
db.commit()
