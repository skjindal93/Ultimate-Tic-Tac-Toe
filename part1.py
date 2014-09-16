import tictactoe as utic
import game
import copy
import sys as sysalias
from timeout import timeout,timer
# apt-get install python-mysqldb for this module
#import MySQLdb
import random

def nop(*arg):
        return
 
_open = __builtins__.open
__builtins__.open = nop
__builtins__.file = nop
__builtins__.eval = nop
__builtins__.execfile = nop
__builtins__.reload = nop



#parser = argparse.ArgumentParser()
#parser.add_argument("--id",help="ID of player.")
#args = parser.parse_args()

## Im assuming a table Id(int),IfWon(bool),Moves(string),Result(string),Score(int)
#db = MySQLdb.connect(host="localhost",user="trystiit_uttt",passwd="uttt@vindy2014",db="trystiit_ultimate")
#cursor = db.cursor()

timeP2 = [5,0]

def ifSmallWin(State,I,J,Player):
        def orfunc(x,y):        return x or y
        def andfunc(x,y):       return x and y
        def helper(x,player):
                if x == None:
                        return False
                elif x.id == player.id:
                        return True
                else:
                        return False
 
        horizontalwin = reduce(orfunc, [True if reduce(andfunc,[True if helper(State[0][I][J][i][j],Player) else False for j in [1,0,2]]) else False for i in [1,0,2]])
        verticalwin = reduce(orfunc, [True if reduce(andfunc,[True if helper(State[0][I][J][i][j],Player) else False for j in [1,0,2]]) else False for i in [1,0,2]])
        diagonal1win = reduce(andfunc, [ True if helper(State[0][I][J][i][j],Player) else False for i in [1,0,2]])
        diagonal2win = reduce(andfunc, [ True if helper(State[0][I][J][i][j],Player) else False for i in [1,0,2]])
        return horizontalwin or diagonal1win or verticalwin or diagonal2win
 

# Returns true if there exists empty positions on the smaller board at I,J.
def checkEmpty(State,I,J):
	return reduce((lambda x,y : x or y), [True if (State[0][I][J][i][j]==None) else False for i in xrange(3) for j in xrange(3)])


class AIPlayer(game.Player):
	def __init__(self,id):
		super(AIPlayer, self).__init__(id)


