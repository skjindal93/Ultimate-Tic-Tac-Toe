def getMove(self,State,PlayerList=[]):
	I,J = State[1]
	board = (I,J);
	initialState = True
	def checkP2(l,m,n,o):
		return State[0][l][m][n][o] != None and State[0][l][m][n][o] != self
	def checkWin(P,Q):
		for s in xrange(3):
			if State[0][P][Q][s][0] == self and State[0][P][Q][s][1]==self and State[0][P][Q][s][2] == None: return s,2
			if State[0][P][Q][s][1] == self and State[0][P][Q][s][2]==self and State[0][P][Q][s][0] == None: return s,0
			if State[0][P][Q][s][2] == self and State[0][P][Q][s][0]==self and State[0][P][Q][s][1] == None: return s,1
		for s in xrange(3):
			if State[0][P][Q][0][s] == self and State[0][P][Q][1][s]==self and State[0][P][Q][2][s] == None: return 2,s
			if State[0][P][Q][1][s] == self and State[0][P][Q][2][s]==self and State[0][P][Q][0][s] == None: return 0,s
			if State[0][P][Q][2][s] == self and State[0][P][Q][0][s]==self and State[0][P][Q][1][s] == None: return 1,s
		if State[0][P][Q][0][0] == self and State[0][P][Q][1][1]==self and State[0][P][Q][2][2] == None: return 2,2
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][2]==self and State[0][P][Q][0][0] == None: return 0,0
		if State[0][P][Q][2][2] == self and State[0][P][Q][0][0]==self and State[0][P][Q][1][1] == None: return 1,1
		if State[0][P][Q][0][2] == self and State[0][P][Q][1][1]==self and State[0][P][Q][2][0] == None: return 2,0
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][0]==self and State[0][P][Q][0][2] == None: return 0,2
		if State[0][P][Q][2][0] == self and State[0][P][Q][0][2]==self and State[0][P][Q][1][1] == None: return 1,1
		return -1,-1
	def getGlobalWinList():
		checkList = []
		for s in xrange(3):
			if ifSmallWin(State,s,0,self) and ifSmallWin(State,s,1,self) and not ifSmallWin(State,s,2,self) : checkList.append((s,2))
			if ifSmallWin(State,s,1,self) and ifSmallWin(State,s,2,self) and not ifSmallWin(State,s,0,self) : checkList.append((s,0))
			if ifSmallWin(State,s,2,self) and ifSmallWin(State,s,0,self) and not ifSmallWin(State,s,1,self) : checkList.append((s,1))
		for s in xrange(3):
			if ifSmallWin(State,0,s,self) and ifSmallWin(State,1,s,self) and not ifSmallWin(State,2,s,self) : checkList.append((2,s))
			if ifSmallWin(State,1,s,self) and ifSmallWin(State,2,s,self) and not ifSmallWin(State,0,s,self) : checkList.append((0,s))
			if ifSmallWin(State,2,s,self) and ifSmallWin(State,0,s,self) and not ifSmallWin(State,1,s,self) : checkList.append((1,s))
		if ifSmallWin(State,0,0,self) and ifSmallWin(State,1,1,self) and not ifSmallWin(State,2,2,self) : checkList.append((2,2))
		if ifSmallWin(State,1,1,self) and ifSmallWin(State,2,2,self) and not ifSmallWin(State,0,0,self) : checkList.append((0,0))
		if ifSmallWin(State,2,2,self) and ifSmallWin(State,0,0,self) and not ifSmallWin(State,1,1,self) : checkList.append((1,1))
		if ifSmallWin(State,0,2,self) and ifSmallWin(State,1,1,self) and not ifSmallWin(State,2,0,self) : checkList.append((2,0))
		if ifSmallWin(State,1,1,self) and ifSmallWin(State,2,0,self) and not ifSmallWin(State,0,2,self) : checkList.append((0,2))
		if ifSmallWin(State,2,0,self) and ifSmallWin(State,0,2,self) and not ifSmallWin(State,1,1,self) : checkList.append((1,1))
		return checkList
	def getGlobalLoseList():
		checkList = []
		p2 = self
		for player in PlayerList:
			if not player == self:
				p2 = player
		for s in xrange(3):
			if ifSmallWin(State,s,0,p2) and ifSmallWin(State,s,1,p2) and not ifSmallWin(State,s,2,p2) : checkList.append((s,2))
			if ifSmallWin(State,s,1,p2) and ifSmallWin(State,s,2,p2) and not ifSmallWin(State,s,0,p2) : checkList.append((s,0))
			if ifSmallWin(State,s,2,p2) and ifSmallWin(State,s,0,p2) and not ifSmallWin(State,s,1,p2) : checkList.append((s,1))
		for s in xrange(3):
			if ifSmallWin(State,0,s,p2) and ifSmallWin(State,1,s,p2) and not ifSmallWin(State,2,s,p2) : checkList.append((2,s))
			if ifSmallWin(State,1,s,p2) and ifSmallWin(State,2,s,p2) and not ifSmallWin(State,0,s,p2) : checkList.append((0,s))
			if ifSmallWin(State,2,s,p2) and ifSmallWin(State,0,s,p2) and not ifSmallWin(State,1,s,p2) : checkList.append((1,s))
		if ifSmallWin(State,0,0,p2) and ifSmallWin(State,1,1,p2) and not ifSmallWin(State,2,2,p2) : checkList.append((2,2))
		if ifSmallWin(State,1,1,p2) and ifSmallWin(State,2,2,p2) and not ifSmallWin(State,0,0,p2) : checkList.append((0,0))
		if ifSmallWin(State,2,2,p2) and ifSmallWin(State,0,0,p2) and not ifSmallWin(State,1,1,p2) : checkList.append((1,1))
		if ifSmallWin(State,0,2,p2) and ifSmallWin(State,1,1,p2) and not ifSmallWin(State,2,0,p2) : checkList.append((2,0))
		if ifSmallWin(State,1,1,p2) and ifSmallWin(State,2,0,p2) and not ifSmallWin(State,0,2,p2) : checkList.append((0,2))
		if ifSmallWin(State,2,0,p2) and ifSmallWin(State,0,2,p2) and not ifSmallWin(State,1,1,p2) : checkList.append((1,1))
		return checkList
	def checkLose(P,Q):
		for s in xrange(3):
			if checkP2(P,Q,s,0) and checkP2(P,Q,s,1)and State[0][P][Q][s][2] == None: return s,2
			if checkP2(P,Q,s,1) and checkP2(P,Q,s,2)and State[0][P][Q][s][0] == None: return s,0
			if checkP2(P,Q,s,2) and checkP2(P,Q,s,0)and State[0][P][Q][s][1] == None: return s,1
		for s in xrange(3):
			if checkP2(P,Q,0,s) and checkP2(P,Q,1,s)and State[0][P][Q][2][s] == None: return 2,s
			if checkP2(P,Q,1,s) and checkP2(P,Q,2,s)and State[0][P][Q][0][s] == None: return 0,s
			if checkP2(P,Q,2,s) and checkP2(P,Q,0,s)and State[0][P][Q][1][s] == None: return 1,s
		if checkP2(P,Q,0,0) and checkP2(P,Q,1,1)and State[0][P][Q][2][2] == None: return 2,2
		if checkP2(P,Q,1,1) and checkP2(P,Q,2,2)and State[0][P][Q][0][0] == None: return 0,0
		if checkP2(P,Q,2,2) and checkP2(P,Q,0,0)and State[0][P][Q][1][1] == None: return 1,1
		if checkP2(P,Q,0,2) and checkP2(P,Q,1,1)and State[0][P][Q][2][0] == None: return 2,0
		if checkP2(P,Q,1,1) and checkP2(P,Q,2,0)and State[0][P][Q][0][2] == None: return 0,2
		if checkP2(P,Q,2,0) and checkP2(P,Q,0,2)and State[0][P][Q][1][1] == None: return 1,1
		return -1,-1
	def getAdjacent(P,Q):
		for s in xrange(3):
			if State[0][P][Q][s][0] == self and State[0][P][Q][s][1]==None and State[0][P][Q][s][2] == None: return s,2
			if State[0][P][Q][s][1] == self and State[0][P][Q][s][2]==None and State[0][P][Q][s][0] == None: return s,0
			if State[0][P][Q][s][2] == self and State[0][P][Q][s][0]==None and State[0][P][Q][s][1] == None: return s,1
		for s in xrange(3):
			if State[0][P][Q][0][s] == self and State[0][P][Q][1][s]== None and State[0][P][Q][2][s] == None: return 2,s
			if State[0][P][Q][1][s] == self and State[0][P][Q][2][s]==None and State[0][P][Q][0][s] == None: return 0,s
			if State[0][P][Q][2][s] == self and State[0][P][Q][0][s]==None and State[0][P][Q][1][s] == None: return 1,s
		if State[0][P][Q][0][0] == self and State[0][P][Q][1][1]==None and State[0][P][Q][2][2] == None: return 2,2
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][2]==None and State[0][P][Q][0][0] == None: return 0,0
		if State[0][P][Q][2][2] == self and State[0][P][Q][0][0]==None and State[0][P][Q][1][1] == None: return 1,1
		if State[0][P][Q][0][2] == self and State[0][P][Q][1][1]==None and State[0][P][Q][2][0] == None: return 2,0
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][0]==None and State[0][P][Q][0][2] == None: return 0,2
		if State[0][P][Q][2][0] == self and State[0][P][Q][0][2]==None and State[0][P][Q][1][1] == None: return 1,1
		return -1,-1
	def getAdjacencyList(P,Q):
		aList = []
		for s in xrange(3):
			if State[0][P][Q][s][0] == self and State[0][P][Q][s][1]==None and State[0][P][Q][s][2] == None: aList.append((s,2))
			if State[0][P][Q][s][1] == self and State[0][P][Q][s][2]==None and State[0][P][Q][s][0] == None: aList.append((s,0))
			if State[0][P][Q][s][2] == self and State[0][P][Q][s][0]==None and State[0][P][Q][s][1] == None: aList.append((s,1))
		for s in xrange(3):
			if State[0][P][Q][0][s] == self and State[0][P][Q][1][s]== None and State[0][P][Q][2][s] == None: aList.append((2,s))
			if State[0][P][Q][1][s] == self and State[0][P][Q][2][s]==None and State[0][P][Q][0][s] == None: aList.append((0,s))
			if State[0][P][Q][2][s] == self and State[0][P][Q][0][s]==None and State[0][P][Q][1][s] == None: aList.append((1,s))
		if State[0][P][Q][0][0] == self and State[0][P][Q][1][1]==None and State[0][P][Q][2][2] == None: aList.append((2,2))
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][2]==None and State[0][P][Q][0][0] == None: aList.append((0,0))
		if State[0][P][Q][2][2] == self and State[0][P][Q][0][0]==None and State[0][P][Q][1][1] == None: aList.append((1,1))
		if State[0][P][Q][0][2] == self and State[0][P][Q][1][1]==None and State[0][P][Q][2][0] == None: aList.append((2,0))
		if State[0][P][Q][1][1] == self and State[0][P][Q][2][0]==None and State[0][P][Q][0][2] == None: aList.append((0,2))
		if State[0][P][Q][2][0] == self and State[0][P][Q][0][2]==None and State[0][P][Q][1][1] == None: aList.append((1,1))
		return aList
		
	def globalCheckWin():
		for X,Y in [(p,q) for p in xrange(3) for q in xrange(3)]:
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = checkWin(X,Y)
			if not r==-1 and not o==-1:
				return X,Y,r,o
		return -1,-1,-1,-1
	def globalCheckLose():
		for X,Y in [(p,q) for p in xrange(3) for q in xrange(3)]:
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = checkLose(X,Y)
			if not r==-1 and not o==-1:
				return X,Y,r,o
			print "not losing for " + str(X)+","+str(Y)+","+str(r)+","+str(o);
		return -1,-1,-1,-1
	def getGlobalAdjacent():
		for X,Y in [(p,q) for p in xrange(3) for q in xrange(3)]:
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = getAdjacent(X,Y)
			if not r==-1 and not o==-1:
				return X,Y,r,o
		return -1,-1,-1,-1
	def adjacentLogic(P,Q):
		aList = getAdjacencyList(P,Q)
		winList = getGlobalWinList()
		loseList = getGlobalLoseList()
		for X in aList:
			i=X[0]
			j=X[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) or not checkEmpty(State,i,j): continue
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) and checkEmpty(State,i,j): 
				r,o = checkWin(i,j)
				if not r==-1 and not o==-1: continue
				r,o = checkLose(i,j)
				if not r==-1 and not o==-1: continue
				if X in winList: continue
				if X in loseList: continue
			if not i==-1 and not j==-1:
				return i,j
		for X in aList:
			i=X[0]
			j=X[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) or not checkEmpty(State,i,j): continue
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) and checkEmpty(State,i,j): 
				r,o = checkWin(i,j)
				if not r==-1 and not o==-1 and X in winList: continue
				r,o = checkLose(i,j)
				if not r==-1 and not o==-1: continue
				if X in loseList: continue
			if not i==-1 and not j==-1:
				return i,j
		for X in aList:
			i=X[0]
			j=X[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) or not checkEmpty(State,i,j): continue
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) and checkEmpty(State,i,j): 
				r,o = checkWin(i,j)
				if not r==-1 and not o==-1 and X in winList: continue
				r,o = checkLose(i,j)
				if not r==-1 and not o==-1 and X in loseList: continue
			if not i==-1 and not j==-1:
				return i,j
		for X in aList:
			i=X[0]
			j=X[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) or not checkEmpty(State,i,j): continue
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,i,j,player) else False for player in PlayerList]) and checkEmpty(State,i,j):
				r,o = checkLose(i,j)
				if not r==-1 and not o==-1 and X in loseList: continue
			if not i==-1 and not j==-1:
				return i,j
		for X in aList:
			i=X[0]
			j=X[1]
			if (True):
				r,o = checkLose(i,j)
				if not r==-1 and not o==-1 and X in loseList: continue
			if not i==-1 and not j==-1:
				return i,j
		return -1,-1
	def logic():
		winList = getGlobalWinList()
		for Xt in winList:
			X = Xt[0]
			Y = Xt[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = checkWin(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
		loseList = getGlobalLoseList()
		for Xt in loseList:
			X = Xt[0]
			Y = Xt[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = checkLose(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
			r,o = checkWin(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
		for Xt in winList:
			X = Xt[0]
			Y = Xt[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = checkLose(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
			r,o = adjacentLogic(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
		for Xt in loseList:
			X = Xt[0]
			Y = Xt[1]
			if reduce(lambda x,y : x or y, [True if ifSmallWin(State,X,Y,player) else False for player in PlayerList]) or not checkEmpty(State,X,Y): continue
			r,o = adjacentLogic(X,Y)
			if not r==-1 and not o==-1: return X,Y,r,o
		return -1,-1,-1,-1
	for X,Y in [(p,q) for p in xrange(3) for q in xrange(3)]:
		for x,y in [(p,q) for p in xrange(3) for q in xrange(3)]:
			if State[0][X][Y][x][y] != None:
				initialState = False
				break
				break
	if initialState == True:
		return 1,1,1,1
	elif not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		if State[0][I][J][I][J] == None:
			return I,J,I,J
		elif State[0][I][J][1][1] == None and not reduce(lambda x,y : x or y, [True if ifSmallWin(State,1,1,player) else False for player in PlayerList]):
			return I,J,1,1
		else:
			i,j = checkWin(I,J)
			if not i==-1 and not j==-1:
				print "Placing through local win"
				return I,J,i,j
			i,j = checkLose(I,J)
			if not i==-1 and not j==-1:
				print "Placing through local lose"
				return I,J,i,j
			i,j = adjacentLogic(I,J)
			if not i==-1 and not j==-1:
				print "Placing through local adj logic"
				return I,J,i,j
			
	else:
		P,Q,i,j = logic()
		if not P==-1 and not Q==-1 and not i==-1 and not j==-1:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,P,Q,player) else False for player in PlayerList]):
				print "Placing through logic"
				return P,Q,i,j
		P,Q,i,j = globalCheckWin()
		if not P==-1 and not Q==-1 and not i==-1 and not j==-1:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,P,Q,player) else False for player in PlayerList]):
				print "Placing through global win logic"
				return P,Q,i,j
		P,Q,i,j = globalCheckLose()
		if not P==-1 and not Q==-1 and not i==-1 and not j==-1:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,P,Q,player) else False for player in PlayerList]):
				print "Placing through global lose logic"
				return P,Q,i,j
		P,Q,i,j = getGlobalAdjacent()
		if not P==-1 and not Q==-1 and not i==-1 and not j==-1:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,P,Q,player) else False for player in PlayerList]):
				print "Placing through global adj logic"
				return P,Q,i,j
	print "Placing Randomly"
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		while True:
			i,j  = random.randint(0,2), random.randint(0,2)
			if State[0][I][J][i][j] == None:
				return I,J,i,j
	else:
		for x,y in [(I,J) for I in xrange(3) for J in xrange(3)]:
			if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,x,y,player) else False for player in PlayerList]) and checkEmpty(State,x,y):
				while True:
					i,j  = random.randint(0,2), random.randint(0,2)
					if State[0][x][y][i][j] == None:
						return x,y,i,j
	pass