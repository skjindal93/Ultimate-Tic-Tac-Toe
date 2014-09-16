def move(self, player, State, pos):
	oldp = State[0][pos[0]][pos[1]][pos[2]][pos[3]]
	olds = State[1]
	State[0][pos[0]][pos[1]][pos[2]][pos[3]] = player
	return ((State[0], (pos[2],pos[3])), pos, oldp, olds)

def unmove(self, obj):
	State, pos, oldp, olds = obj
	State[0][pos[0]][pos[1]][pos[2]][pos[3]] = oldp
	return (State[0], olds)

def ok(self, State, pos, other):
	return not (ifSmallWin(State,pos[0],pos[1],self) or ifSmallWin(State,pos[0],pos[1],other) or not checkEmpty(State, pos[0],pos[1]))
def wassup(self, State, other):
	pos = State[1]
	if not self.ok(State, pos, other):
		pos = None
	return pos

def won(self, box, player):
	for i in range(3):
		if (box[i][0] == player and box[i][1] == player and box[i][2] == player):
			return True
	for i in range(3):
		if (box[0][i] == player and box[1][i] == player and box[2][i] == player):
			return True
	if (box[0][0] == player and box[1][1] == player and box[2][2] == player):
		return True
	if (box[0][2] == player and box[1][1] == player and box[2][0] == player):
		return True
	return False

def winnable(self, box, player):
	v = 0
	for i,j in [(x,y) for x in range(3) for y in range(3)]:
		if box[i][j] == None:
			box[i][j] = player
			if self.won(box, player):
				v += 1
			box[i][j] = None
	return v

def predict(self, box, player):
	for i,j in [(x,y) for x in range(3) for y in range(3)]:
		if box[i][j] == None:
			box[i][j] = player
			if self.won(box, player):
				box[i][j] = None
				return True
			box[i][j] = None
	return False

def util(self, State, other, supp):
	v = 0
	next = State[0][State[1][0]][State[1][1]]
	for box in [(i,j) for i in range(3) for j in range(3)]:
		if ifSmallWin(State, box[0], box[1], other):
			v -= 20
		elif ifSmallWin(State, box[0], box[1], self):
			v += 10
		elif not self.won(next, other) and self.predict(State[0][box[0]][box[1]], self):
			v += 4
	if not self.won(next, other) and self.predict(next, self):
		v += 5
	if(not self.ok(State, State[1], other)):
		v += 5
	return v

def value(self, State, other, depth = 2):
	supp = self.wassup(State, other)
	if depth == 0:
		return self.util(State, other, supp)
	if depth % 2 == 1:
		return self.exp(State, other, depth, supp)
	else:
		return self.max(State, other, depth, supp)

def lessofmore(self, arr):
	arr.sort(reverse = True)
	v = 1.0
	m = 1.25
	s = 0.0
	n = 0.0
	for t in arr:
		s += t*v
		n += v
		v *= m
	if (n == 0):
		return 0
	return float(s)/n

def expd(self, State, other, depth, supp):
	val = []
	for x,y in [(i,j) for i in range(3) for j in range(3)]:
		if State[0][supp[0]][supp[1]][x][y] == None:
			ret = self.move(other, State, (supp[0], supp[1], x, y))
			val.append(self.value(ret[0], other, depth - 1))
			State = self.unmove(ret)
	if len(val) == 0:
		return self.util(State, other, supp)
	return self.lessofmore(val)

def exp(self, State, other, depth, supp):
	if supp:
		return self.expd(State, other, depth, supp)
	else:
		val = []
		for supp in [(i,j) for i in range(3) for j in range(3)]:
			if self.ok(State, supp, other):
				val.append(self.expd(State, other, depth, supp))
		if len(val) == 0:
			return self.util(State, other, supp)
		else:
			return self.lessofmore(val)

def maxd(self, State, other, depth, supp):
	val = float("-inf")
	for x,y in [(i,j) for i in range(3) for j in range(3)]:
		if State[0][supp[0]][supp[1]][x][y] == None:
			ret = self.move(self, State, (supp[0], supp[1], x, y))
			val = max(val, self.value(ret[0], other, depth - 1))
			State = self.unmove(ret)
	return val

def max(self, State, other, depth, supp):
	if supp:
		return self.maxd(State, other, depth, supp)
	else:
		val = float("-inf")
		for supp in [(i,j) for i in range(3) for j in range(3)]:
			val = max(val, self.maxd(State, other, depth, supp))
		return val

def getd(self, State, PlayerList, supp):
	val = float("-inf")
	best = None
	depth = 2
	if self == PlayerList[0]:
		other = PlayerList[1]
	else:
		other = PlayerList[0]
	for x,y in [(i,j) for i in range(3) for j in range(3)]:
		if State[0][supp[0]][supp[1]][x][y] == None:
			ret = self.move(self, State, (supp[0], supp[1], x, y))
			nval = self.value(ret[0], other, depth - 1)
			if not best or nval > val:
				best = (supp[0], supp[1], x, y)
				val = nval
			State = self.unmove(ret)
	return (val, best)

def getMove(self,State,PlayerList=[]):
	if self == PlayerList[0]:
		other = PlayerList[1]
	else:
		other = PlayerList[0]
	supp = self.wassup(State, other)
	if supp:
		return self.getd(State, PlayerList, supp)[1]
	else:
		val = float("-inf")
		best = None
		for supp in [(i,j) for i in range(3) for j in range(3)]:
			if checkEmpty(State, supp[0], supp[1]):
				ret = self.getd(State, PlayerList, supp)
				if not best or (ret[0] > val):
					val = ret[0]
					best = ret[1]
		if best:
			return best
	I,J = State[1]
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