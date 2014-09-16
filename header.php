<?php
session_start();
require_once ("config.php");
require_once ("database.php");
require_once ("user.php");
require_once ("session.php");

?>

<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Ultimate Tic Tac Toe</title>
		<meta name="description" content="Ultimate Tic Tac Toe" />
		<meta name="keywords" content="ultimate tic tac toe, tryst iitd" />
		<meta name="author" content="Tryst IITD" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="css/normalize.css" />
		<link rel="stylesheet" type="text/css" href="css/demo.css" />
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		
		<script src="js/modernizr.custom.js"></script>
	</head>
	<style type="text/css">
	.error{
		width: 100%;
margin-top: 5%;
text-align: center;
position: absolute;
color: red;
font-size: 20px;
	}
	</style>
	<body>
		<div class="container">
			<ul id="gn-menu" class="gn-menu-main">
				<li class="gn-trigger">
					<a class="gn-icon gn-icon-menu"><span>Menu</span></a>
					<nav class="gn-menu-wrapper">
						<div class="gn-scroller">
							<ul class="gn-menu">
								<li>
									<a class="gn-icon gn-icon-article" href="index.php">Home</a>
								</li>
								<li>
									<a class="gn-icon gn-icon-pictures" href = "leaderboard.php">LeaderBoard</a>
								</li>
								<li><a class="gn-icon gn-icon-cog" href = "rules.php">Rules</a></li>
								<li><a class="gn-icon gn-icon-help" href = "contact.php">Contact Us</a></li>
							</ul>
						</div><!-- /gn-scroller -->
					</nav>
				</li>
				
				<?php

						echo '<li><a class="codrops-icon codrops-icon-prev" href="uttt.php"><span>Ultimate Tic Tac Toe</span></a></li>';
					
				?>
				<li><a class="codrops-icon codrops-icon-prev" href="https://www.facebook.com/events/604348266319290/"><span>Facebook</span></a></li>
				<li><a class="codrops-icon codrops-icon-prev" href="http://tryst-iitd.com"><span>Tryst</span></a></li>
				
				<?php
					if (!$session->is_logged_in ()) {
						echo '<li  style="float:right;"><a class="codrops-icon codrops-icon-drop" href="register.php"><span>Register</span></a></li>';
echo '<li  style="float:right;"><a class="codrops-icon codrops-icon-drop" href="login.php"><span>Login</span></a></li>';
							  		
					}
					else {
						echo '<li  style="float:right;"><a class="codrops-icon codrops-icon-drop"href="logout.php"><span>Logout</span></a></li>';
				
					}
				?>
				
			</ul> 
		</div><!-- /container -->
		<script src="js/classie.js"></script>
		<script src="js/gnmenu.js"></script>
		<script>
			new gnMenu( document.getElementById( 'gn-menu' ) );
		</script>

	</body>
</html>