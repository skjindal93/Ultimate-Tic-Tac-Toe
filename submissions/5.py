def getMove(self,State,PlayerList=[]):
	I,J = State[1]
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		if State[0][I][J][1][1] == None:
			return I,J,1,1
		if State[0][I][J][0][0] == None:
			return I,J,0,0
		if State[0][I][J][2][2] == None:
			return I,J,2,2
    	while True:
				i,j  = random.randint(0,2), random.randint(0,2)
				if State[0][I][J][i][j] == None:
					return I,J,i,j
	else:
		for x,y in [(I,J) for I in xrange(3) for J in xrange(3)]:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,x,y,player) else False for player in PlayerList]) and checkEmpty(State,x,y):    
				if State[0][I][J][1][1] == None:
					return I,J,1,1
				if State[0][I][J][0][0] == None:
					return I,J,0,0
				if State[0][I][J][2][2] == None:
					return I,J,2,2
				while True:
					i,j  = random.randint(0,2), random.randint(0,2)
					if State[0][x][y][i][j] == None:
						return x,y,i,j				
