<?php
	require_once('header.php');
?>
<style>
header{
	margin-top:6%;
	margin-left: 40%;	
	color:white;
	font-family: 'Lato', Arial, sans-serif;
	line-height: 1.3;
	letter-spacing: 1px;
	font-size: 18px;
}
#rules p
{
	color:white;
	font-family: 'Lato', Arial, sans-serif;
	line-height: 1.3;
	letter-spacing: 1px;
	font-weight: 300;
}
#rules li
{
	color:white;
	font-family: 'Lato', Arial, sans-serif;
	line-height: 1.3;
	font-weight: 300;
	letter-spacing: 1px;
}
#rules b
{
	font-family: 'Lato', Arial, sans-serif;
	letter-spacing: 1px;
	color:white;
}
</style>
<body style="background: #34495e;">
<div>
			<header>
				<h1> Rules for the game </h1>
			</header>
<div id = "rules" style = "margin:8%;font-size:20px;">
<b>About the Event</b>
<p>
We all know that Tic Tac Toe is a solved game and it ends in a draw given, both players play optimal moves. To make the game interesting, a group of mathematicians decided to fill in each square of the board with a smaller Tic-Tac-Toe board and started the game what is now called as Ultimate Tic Tac Toe. So if your brain opens up to a strategic game play then this event is just right for you.
</p>

<b>Problem Statement</b>
<p>
Each square of the Ultimate Tic-Tac-Toe board is indexed at (0,0) top-left and (2,2) at bottom-right.
Each player writes their respective marker in an empty square only.
If a player makes a move at (2,2) inside the square (1,2), then the next player is forced to make his next move inside any of the empty squares of the square (2,2).
If square (2,2) as mentioned above is filled up, then the next player can make a move in any of the squares of the board.
If a player is forced to make a move into a square that is already won, the player can make a move in any of the squares of the board.
If a player marks 3 consecutive squares (horizontally, vertically or diagonally) on any of the squares of Ultimate Tic-Tac-Toe, he wins that square.
The goal is to win any 3 consecutive squares (horizontally, vertically or diagonally) of the Ultimate Tic-Tac-Toe board.
The first player can start on any of the squares of the board.

For more detailed instructions of the game refer <a style="color:white;" href = "http://mathwithbaddrawings.com/2013/06/16/ultimate-tic-tac-toe/">here</a>
</p>
<b>Event Guidelines </b>
<p>
<ul>
<li>You have to work individually.
<li>You need to register for the event to play the game.
<l>Once you have registered for the event you can submit your code by pasting your code in the box provided. A sample code for the bot will be provided for your reference. 
<li>You just need to code the logic for a bot which takes as input a state and the playerlist and returns a 4-tuple.
<li>The State is a 2 tuple whose first position is a 4-D array which stores the player at every board position. So, State[0][I][J][i][j] returns the self if the i,j position of the smaller board at postion I,J in the bigger board is the player itself, None if there is no player, and another instance of class Player if its occupied by another player.
<li>The second position is a 2-tuple which is the position of the smaller board that the previous player has sent you to.
<li>You have to complete the code in the snippet.py file provided to you and upload it on the submission portal. You are not allowed (you can’t) to use any function or data structure not defined in the scope of the function, except for the ifSmallWin and ifCheckEmpty functions defined in the global scope.
<li>The ifSmallWin function takes as argument (State,I,J,Player), where State is of the same type as mentioned in point 5, I,J is the location of the smaller board and Player is an instance of class(or subclass of) Player. It returns True if the board I,J has been won by Player and False otherwise.
<li>The checkEmpty function takes as argument (State,I,J), where all the symbols mean the same thing as in the last point. It returns True if there exists an empty position in the smaller board at I,J and False otherwise.
<li>You have to provide the final code as a Python function. You can code in any language but you must create a Python Wrapper for your program.
<li>The game will be played out automatically and any errors in output will lead to an automatic forfeit of the match. 
<li>You can test your code locally against a random player or a manual player (both implemented in the code provided to you).
<li>To test the player locally, implement the getMove function in class AIplayer in the file main.py. Run the file as python main.py --p1={RP,AP,MP} --p2={RP,MP,AP}, where RP is a random player, MP is a manual player and AP your AI player. Default for p1 is AP and for P2 is RP.
<li>Once you submit your code, you will be able to see your bot’s performance against our bot turn by turn. You can change your bot’s code on the basis of this till 28 Feb.
<li>Your last submission of code before the final deadline (28 Feb) will be considered final and will be considered to generate your final rank.
</ul>
</p>


<b>Evaluation Schema</b>

<ul>
<li>A team wins if any 3 consecutive squares (horizontally, vertically or diagonally) of the ultimate tic-tac-toe board are won . We'll record the score of each user using the following rules:
<li>We will run your bot against our AI bot in the first round. If you win the game you get 100 points.
<li>If you lose the game, you get x*10 points where x is the no. of smaller tic tac toes you won. 
<li>Your bot will play against our bot for fixed no. of matches and the sum total of the scores over these matches along with total no. of smaller tic tac toes won will be considered for generating your ranks.
<li>The top 8 bots in terms of score will qualify for the final round of 8C2 matches among your own bots. Ties in the score will be resolved on the basis of total no. of smaller tic tac toes won.
<li>The final top 3 individuals on the basis of the final round will be declared as winners.
</ul>
<p>
*Any malpractice would lead to straight disqualification. Also, any conflicts will be resolved by the organisers and would be considered as final and binding. 

</p>


<b>Important Dates</b>
<ul>
<li>Online registrations commence - Monday, 17th February 2014
<li>Portal opens - Monday, 17th February 2014
<li>Last date for submission of code - 28 February 2014
<li>Results declaration  - 1 March 2014
</ul>

<b>Prizes</b>
<p>
Cash prizes for top 3 individuals.
Participation certificates for all.
</p>

</div>
</div>
</body>