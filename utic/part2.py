
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

	with open("2.out",'w') as outfile:
		outfile.write(moves)
	## Im assuming a table Id(int),IfWon(bool),IfTie(bool),Moves(string),Result(string),Score(int)
		#if Game.State.winner == None:
		#	#cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),0,1,moves,Game.State.result,Game.score))
		#	outfile.write(moves)
		#elif Game.State.winner.id == 1:
		#	#cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),0,0,moves,Game.State.result,Game.score))
		#elif Game.State.winner.id == 2:
			#cursor.execute("INSERT INTO score VALUES(%s,%s,%s,%s,%s,%s)",(int(args.id),1,0,moves,Game.State.result,Game.score))

	#db.commit()
