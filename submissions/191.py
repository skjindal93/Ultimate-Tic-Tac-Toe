def mini(self,alpha, beta, depth, State,winnerlist , PlayerList=[]):
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		lis = self.getFree(State, I, J)
	else :
		lis = [x for y in [self.getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	
	ret = 1000000000 
	
	other = None
	for x in PlayerList:
		if x != self:
			other = x 

	if len(lis) == 0 or depth  == 0: 
		return self.evaluate(State, winnerlist)

	for candidate in lis: 
		I, J, i, j = candidate
		tempState = copy.deepcopy(State)
		tempState[0][I][J][i][j] = other
		tempState[1] = (i,j)
		temp = self.maxi(alpha, beta, depth-1, tempState, copy.deepcopy(self.updatewinnerlist(tempState,PlayerList,winnerlist)),PlayerList)
		ret = min(temp, ret)
		beta = min(temp, beta)
		State[0][I][J][i][j] = None
		if alpha >= beta:
			return ret
	return ret

def maxi(self,alpha, beta, depth, State,winnerlist, PlayerList=[]):
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		lis = self.getFree(State, I, J)
	else :
		lis = [x for y in [self.getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	ret = -1000000000 
	
	other = None
	for x in PlayerList:
		if x != self:
			other = x 
	if len(lis) == 0 or depth  == 0:
		return self.evaluate(State, winnerlist)

	for candidate in lis: 
		I, J, i, j = candidate
		tempState = copy.deepcopy(State)
		tempState[0][I][J][i][j] = self
		tempState[1] = (i,j)
		temp = self.mini(alpha, beta, depth-1, tempState,copy.deepcopy(self.updatewinnerlist(tempState,PlayerList,winnerlist)), PlayerList)
		ret = max(temp, ret)
		alpha = max(temp, beta)
		State[0][I][J][i][j] = None
		if alpha >= beta:
			return ret
	return ret

def evaluate(self, State,winnerlist):
	cnt = 0
	for i in xrange(3):
		for j in xrange(3):
			if ifSmallWin(State,i,j,self):
				cnt += 1
			elif ifSmallWin(State,i,j,other):
				cnt -=1
	return cnt


def getFree(self,State,I,J): 
	return filter(lambda x: State[0][x[0]][x[1]][x[2]][x[3]] == None ,[(I,J,i,j) for i in xrange(3) for j in xrange(3)])
	
def getMove(self,State,PlayerList=[]):
	self.winnerlist = self.updatewinnerlist(State,PlayerList, self.winnerlist)
	I, J = State[1]
	lis = [] 
	if not reduce(lambda x,y : x or y, [True if ifSmallWin(State,I,J,player) else False for player in PlayerList]) and checkEmpty(State,I,J):
		# print "In here", I, J
		lis = self.getFree(State, I, J)
	else :
		lis = [x for y in [self.getFree(State, i, j) for i in xrange(3) for j in xrange(3)] for x in y]
	
	ret = -1000000000 
	ans = (0,0,0,0)
	other = None
	for x in PlayerList:
		if x != self:
			other = x 

	# print "candidates: "
	
	for candidate in lis: 
		I, J, i, j = candidate
		tempState = copy.deepcopy(State)
		tempState[0][I][J][i][j] = self
		tempState = [tempState[0], (i,j)]
		temp = self.mini(-1000000000, 1000000000, 4,tempState, copy.deepcopy(self.updatewinnerlist(tempState,PlayerList,self.winnerlist)),PlayerList)
		if ret < temp: 
			ans = candidate
			ret = temp
		# print candidate, temp
	# print "About to return", ans
	tempState = copy.deepcopy(State)
	tempState[0][ans[0]][ans[1]][ans[2]][ans[3]] = self
	self.winnerlist = self.updatewinnerlist(tempState,PlayerList,self.winnerlist)
	return ans