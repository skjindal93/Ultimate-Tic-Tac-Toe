import tictactoe as utic
import game
import argparse
import copy
from timeout import timeout,timer
import random
import math

# apt-get install python-mysqldb for this module
import MySQLdb


parser = argparse.ArgumentParser()
parser.add_argument("--id",help="ID of player.")
args = parser.parse_args()

## I'm assuming a table Id(int),IfWon(bool),Moves(string),Result(string),Score(int)
db = MySQLdb.connect(host="localhost",user="root",passwd="dafadafa",db="uttt")
cursor = db.cursor()

timeP2 = [300,0]

# Returns true if Player has won the smaller Tic-Tac-Toe board at I,J.
def ifSmallWin(State,I,J,Player):
	def orfunc(x,y):	return x or y
	def andfunc(x,y):	return x and y
	horizontalwin = reduce(orfunc, [True if reduce(andfunc,[True if State[0][I][J][i][j]==Player else False for j in xrange(3)]) else False for i in xrange(3)])
	verticalwin = reduce(orfunc, [True if reduce(andfunc,[True if State[0][I][J][j][i]==Player else False for j in xrange(3)]) else False for i in xrange(3)])
	diagonal1win = reduce(andfunc, [ True if State[0][I][J][i][i]==Player else False for i in xrange(3)])
	diagonal2win = reduce(andfunc, [ True if State[0][I][J][2-i][i]==Player else False for i in xrange(3)])
	return horizontalwin or diagonal1win or verticalwin or diagonal2win


# Returns true if there exists empty positions on the smaller board at I,J.
def checkEmpty(State,I,J):
	return reduce((lambda x,y : x or y), [True if (State[0][I][J][i][j]==None) else False for i in xrange(3) for j in xrange(3)])


class AIPlayer(game.Player):
	def __init__(self,id):
		super(AIPlayer, self).__init__(id)

	@timeout(timeP2)
	def getMove(self,State,PlayerList=[]):
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



if __name__ == '__main__' :

	# if not args.p1 or args.p1 == 'AP':
	# 	P1 = AIPlayer(1)
	# elif args.p1 == 'RP':
	# 	P1 = utic.RandomPlayer(1)
	# elif args.p1 == 'OP':
	# 	P1 = utic.OurPlayer(1)
	# else:
	# 	raise game.Error("Please select a valid player.")

	P1 = utic.OurPlayer(1)
	P2 = AIPlayer(2)

	# if not args.p2 or args.p2 == 'RP':
	# 	P2 = utic.RandomPlayer(2)
	# elif args.p2 == 'AP':
	# 	P2 = AIPlayer(2)
	# elif args.p2 == 'OP':
	# 	P2 = utic.OurPlayer(2)
	# else:
	# 	raise game.Error("Please select a valid player.")


	State = utic.State([P1,P2],2)
	# Change the third argument to True to print the gamestate after every move.
	# Change the fourth argument to True to wait for keyboard input to move to the next state.
	# Press enter to advance the game by two moves.
	Game = utic.TicTacToeGame(State, [P1,P2],False,False)

	Game.run()
	Game.genScore()
	print Game.score
	moves = ""
	for i in xrange(len(Game.State.moves) - 1):
		moves += str(Game.State.moves[i] + ",")
	moves += str(Game.State.moves[len(Game.State.moves)-1])

	## I'm assuming a table Id(int),IfWon(bool),IfTie(bool),Moves(string),Result(string),Score(int)
	print Game.State.winner
	if Game.State.winner == None:
		cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),0,1,moves,Game.State.result,Game.score))
	elif Game.State.winner.id == 1:
		cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),0,0,moves,Game.State.result,Game.score))
	elif Game.State.winner.id == 2:
		cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),1,0,moves,Game.State.result,Game.score))

	db.commit()
