def getMove(self,State,PlayerList=[]):
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		lis = getFree(State, I, J)
	else :
		lis = [x for y in [getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	ret = -1000000000 
	ans = (0,0,0,0)
	other = None
	for x in PlayerList:
		if x != self:
			other = x 

	if len(lis) == 0 or depth  == 0: 
		return eval(self, other, State)
	for candidate in lis: 
		I, J, i, j = candidate
		State[0][I][J][i][j] = self
		State[1] = (i,j)
		temp = mini(-1000000000, 1000000000, 4, other, State, PlayerList)
		if ret < temp: 
			ans = candidate
			ret = temp
		alpha = max(temp, beta)
		State[0][I][J][i][j] = None
	return ans

def mini(alpha, beta, depth, self, State, PlayerList=[]):
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		lis = getFree(State, I, J)
	else :
		lis = [x for y in [getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	
	ret = 1000000000 
	
	other = None
	for x in PlayerList:
		if x != self:
			other = x 

	if len(lis) == 0 or depth  == 0: 
		return eval(self, other, State)

	for candidate in lis: 
		I, J, i, j = candidate
		State[0][I][J][i][j] = self
		State[1] = (i,j)
		temp = maxi(alpha, beta, depth-1, other, State, PlayerList)
		ret = min(temp, ret)
		beta = min(temp, beta)
		State[0][I][J][i][j] = None
		if alpha >= beta:
			return ret
	return ret

def maxi(alpha, beta, depth, self, State, PlayerList=[]):
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		lis = getFree(State, I, J)
	else :
		lis = [x for y in [getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	ret = -1000000000 
	
	other = None
	for x in PlayerList:
		if x != self:
			other = x 
	if len(lis) == 0 or depth  == 0: 
		return eval(self, other, State)

	for candidate in lis: 
		I, J, i, j = candidate
		State[0][I][J][i][j] = self
		State[1] = (i,j)
		temp = mini(alpha, beta, depth-1, other, State, PlayerList)
		ret = max(temp, ret)
		alpha = max(temp, beta)
		State[0][I][J][i][j] = None
		if alpha >= beta:
			return ret
	return ret

def eval(self, other, State):
	cnt = 0
	for i in xrange(3):
		for j in xrange(3):
			if ifSmallWin(State,i,j,self):
				cnt += 1
			elif ifSmallWin(State,i,j,other):
				cnt -=1


def getFree(State,I,J): 
	return filter(lambda x: State[0][x[0]][x[1]][x[2]][x[3]] != None ,[(I,J,i,j) for i in xrange(3) for j in xrange(3)])
