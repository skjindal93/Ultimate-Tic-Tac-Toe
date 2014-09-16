def getMove(self,State,PlayerList=[]):
	I,J = State[1]
	mymoves=[(1,1),(0,0),(0,2),(2,0),(2,2),(0,1),(1,0),(1,2),(2,1)]
	if (not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList])) and (checkEmpty(State,I,J)):
		for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
			if State[0][I][J][i][j] == None:
				State[0][I][J][i][j] = P1
				if ifSmallWin(State,I,J,P1):
					State[0][I][J][i][j] = None
					return I,J,i,j
				State[0][I][J][i][j] = None
		for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
			if State[0][I][J][i][j] == None:
				State[0][I][J][i][j] = P2
				if ifSmallWin(State,I,J,P2):
					State[0][I][J][i][j] = None
					return I,J,i,j
				State[0][I][J][i][j] = None
		for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
			if State[0][I][J][i][j] == None:
				flag = False
				State[0][I][J][i][j] = P1
				for k,l in [(m,n) for m in xrange(3) for n in xrange(3)]:
					if State[0][I][J][k][l] == None:
						State[0][I][J][k][l] = P1
						if ifSmallWin(State,I,J,P1):
							State[0][I][J][k][l] = None
							flag = True
							break
						State[0][I][J][k][l] = None
				if flag:
					for k,l in [(m,n) for m in xrange(3) for n in xrange(3)]:
						if State[0][i][j][k][l] == None:
							State[0][i][j][k][l] = P2
							if ifSmallWin(State,i,j,P2):
								State[0][i][j][k][l] = None
								flag = False
								break
							State[0][i][j][k][l] = None
				if flag:
					State[0][I][J][i][j] = None
					return I,J,i,j
				State[0][I][J][i][j] = None					
		for i,j in mymoves:
			if State[0][I][J][i][j] == None:
				flag = True
				for k,l in [(x,y) for x in xrange(3) for y in xrange(3)]:
					if State[0][i][j][k][l] == None:
						State[0][i][j][k][l] = P2
						if ifSmallWin(State,i,j,P2):
							State[0][i][j][k][l] = None
							flag = False
							break
						State[0][i][j][k][l] = None	
				if flag:
					return I,J,i,j
		for i,j in mymoves:
			if State[0][I][J][i][j] == None:
				return I,J,i,j
							
	else:
		for a,b in mymoves:
			if not reduce(lambda a,b : a or b, [True if ifSmallWin(State,a,b,player) else False for player in PlayerList]) and checkEmpty(State,a,b):
				for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
					if State[0][a][b][i][j] == None:
						State[0][a][b][i][j] = P1
						if ifSmallWin(State,a,b,P1):
							State[0][a][b][i][j] = None
							return a,b,i,j
						State[0][a][b][i][j] = None
		for a,b in mymoves:
			if not reduce(lambda a,b : a or b, [True if ifSmallWin(State,a,b,player) else False for player in PlayerList]) and checkEmpty(State,a,b):
				for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
					if State[0][a][b][i][j] == None:
						State[0][a][b][i][j] = P2
						if ifSmallWin(State,a,b,P2):
							State[0][a][b][i][j] = None
							return a,b,i,j
						State[0][a][b][i][j] = None
		for a,b in mymoves:
			if not reduce(lambda a,b : a or b, [True if ifSmallWin(State,a,b,player) else False for player in PlayerList]) and checkEmpty(State,a,b):
				for i,j in [(x,y) for x in xrange(3) for y in xrange(3)]:
					if State[0][a][b][i][j] == None:
						flag = False
						State[0][a][b][i][j] = P1
						for k,l in [(m,n) for m in xrange(3) for n in xrange(3)]:
							if State[0][a][b][k][l] == None:
								State[0][a][b][k][l] = P1
								if ifSmallWin(State,I,J,P1):
									State[0][a][b][k][l] = None
									flag = True
									break
								State[0][a][b][k][l] = None
						if flag:
							for k,l in [(m,n) for m in xrange(3) for n in xrange(3)]:
								if State[0][i][j][k][l] == None:
									State[0][i][j][k][l] = P2
									if ifSmallWin(State,i,j,P2):
										State[0][i][j][k][l] = None
										flag = False
										break
									State[0][i][j][k][l] = None
						if flag:
							State[0][a][b][i][j] = None
							return a,b,i,j
						State[0][a][b][i][j] = None
		for a,b in mymoves:
			if not reduce(lambda a,b : a or b, [True if ifSmallWin(State,a,b,player) else False for player in PlayerList]) and checkEmpty(State,a,b):
				for i,j in mymoves:
					if State[0][a][b][i][j] == None:
						flag = True
						for k,l in [(x,y) for x in xrange(3) for y in xrange(3)]:
							if State[0][i][j][k][l] == None:
								State[0][i][j][k][l] = P2
								if ifSmallWin(State,i,j,P2):
									State[0][i][j][k][l] = None
									flag = False
									break
								State[0][i][j][k][l] = None	
						if flag:
							return a,b,i,j
		for a,b in mymoves:
			if not reduce(lambda a,b : a or b, [True if ifSmallWin(State,a,b,player) else False for player in PlayerList]) and checkEmpty(State,a,b):
				for i,j in mymoves:
					if State[0][a][b][i][j] == None:
						return a,b,i,j