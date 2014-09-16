<?php
include ("header.php");
if ($session->is_logged_in ()) {
	printf ( "<script>location.href='index.php'</script>" );
}
if (isset ( $_POST ['submit'] )) {
	if (isset ( $_POST ['password'] )) {
		$password = htmlspecialchars($_POST ['password']);
		if (strcmp ( $password, htmlspecialchars($_POST ['confirmpassword'] )) != 0) {
			$password = "";
		}
	} else {
		$password = "";
	}
	$message = "";
	if (empty ( $password )) {
		$message = "Registration error." . "<br />";
	} else {
		$user = new User ();
		$user->username = htmlspecialchars($_POST ['username']);
		$user->password = $password;
		$user->name = htmlspecialchars($_POST ['name']);
		$user->address = htmlspecialchars($_POST ['address']);
		$user->email = htmlspecialchars($_POST ['email']);
		$user->phone = htmlspecialchars($_POST ['phone']);
		$user->collegeid = htmlspecialchars($_POST ['collegeid']);
		$user->college = htmlspecialchars($_POST ['college']);
		$user->city = htmlspecialchars($_POST ['city']);
		$user->country = htmlspecialchars($_POST ['country']);
		$user->score = 0;
		
		if (! $user->insert ()) {

			$message .= "Error! The registration was not proceeded." . "<br />";
		} else {
			printf ( "<script>location.href='index.php'</script>" );
			$message .= "Registration Successful!" . "<br />";
		}
	}
	
	if (isset ( $message )) {
		echo '<div class="error">'.$message.'</div>';
	}
} else {
	?>
<link rel="stylesheet" type="text/css" href="css/default.css"/>
<div class="container1" style="background:black;color:white;">
		<div class="main">
					<form action="register.php" method="post" style="margin-top:2%;" class="cbp-mc-form">
						<div class="cbp-mc-column">
							<label for="username">Username*</label>
		  					<input type="text" id="first_name" name="username" required="required" placeholder="Jonathan">
		  					<label for="password">Password*</label>
		  					<input type="password" id="password" name="password" required="required" placeholder="*****" maxlength="100">
		  					<label for="confirmpassword">Confirm Password*</label>
		  					<input type="password" id="confirmpassword" name="confirmpassword" required="required" maxlength="100" placeholder="*****">
		  					<label for="name">Name*</label>
		  					<input type="text" id="name" name="name" required="required" placeholder="Jonathan">
		  				</div>
		  				<div class="cbp-mc-column">
		  					<label for="address">Address</label>
	  						<textarea id="address" name="address"></textarea>
		  					<label for="email">Email Address*</label>
		  					<input type="text" id="email" name="email" required="required" placeholder="jon@doe.com" maxlength="100">
		  					<label for="city">City</label>
		  					<input type="text" id="city" name="city" placeholder="Delhi" maxlength="100">
		  				</div>
		  				<div class="cbp-mc-column">
		  					<label for="country">Country</label>
		  					<input type="text" id="country" name="country" placeholder="India" maxlength="100">
		  					<label for="college">College Name*</label>
		  					<input type="text" id="college" name="college" required="required" maxlength="100"></input>
		  					<label for="collegeid">Student ID*</label>
		  					<input type="text" id="collegeid" name="collegeid" required="required" maxlength="100"></input>
		  				</div>
		  			<div class="cbp-mc-submit-wrap"><input class="cbp-mc-submit" type="submit" value="Register!!" name="submit"/></div>
					</form>
		</div>
</div>

<?php
}
?>
	