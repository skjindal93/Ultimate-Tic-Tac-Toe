<?php
require_once ("header.php");
if ($session->is_logged_in ()) {
	printf ( "<script>location.href='index.php'</script>" );
}
if (isset ( $_POST ['submit'] )) {
	$username = trim ( $_POST ['username'] );
	$password = trim ( $_POST ['password'] );
	
	$found_user = User::authenticate ( $username, $password );
	if ($found_user) {
		$userid = $found_user;
		$session->login ( $userid );
		printf ( "<script>location.href='index.php'</script>" );
	} else {
		$message = "Incorrect Username/Password" . "\n";
	}
	if (isset ( $message )) {
		echo '<div class="error">'.$message.'</div>';
	}
} else {
	$username = "";
	$password = "";
	
	?>

<link rel="stylesheet" type="text/css" href="css/default.css"/>
<body style="background:black;">
<div class="container1" style="color:white;">
		<div class="main">
					<form action="login.php" method="post" style="margin-top:2%;" class="cbp-mc-form">
						<div class="cbp-mc-column" style="float:none;margin:0 auto;">
							<label for="username">Username</label>
		  					<input type="text" id="first_name" name="username" placeholder="Jonathan" maxlength="30">
		  					<label for="password">Password</label>
		  					<input type="password" id="password" name="password" placeholder="*****" maxlength="100">
		  				</div>
		  			<div class="cbp-mc-submit-wrap"><input class="cbp-mc-submit" type="submit" value="Login!!" name="submit"/></div>
					</form>
		</div>
</div>
</body>
<?php
}
?>