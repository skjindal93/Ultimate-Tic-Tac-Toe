<?php
require_once ("header.php");
$users = User::show_top ();
?>
<!DOCTYPE html>

<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<link rel="stylesheet" type="text/css" href="css/normalize.css" />
		
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		<link rel="stylesheet" type="text/css" href="css/table.css" />
		
	</head>
	<style type="text/css">
	#leader{
		margin-top:6%;
	margin-left: 40%;	
	color:white;
	font-family: 'Lato', Arial, sans-serif;
	line-height: 1.3;
	letter-spacing: 1px;
	font-size: 30px;
	}
	</style>
	<body  style="background: #34495e;">
		
<body  style="background: #34495e;">
	<div class="container">
	<h1 id="leader"> LeaderBoard</h1>
		<div class="component">
			<table>
				<thead>
					<tr>
						<th>Name</th>
						<th>Score</th>
						<th>College</th>
					</tr>
				</thead>
				<tbody>
	<?php
	for($ii = 0; $ii < count ( $users ); $ii ++) {

		?>
		<tr><td class="user-name"><?php echo $users[$ii]->username; ?></td><td class="user-email"><?php echo $users[$ii]->score; ?></td><td class="user-phone"><?php echo $users[$ii]->college; ?></td></tr>
<?php

	}
	?>
	</tbody>
	</table>
<?php

?>
		<script src="jquery.js"></script>
		<script src="js/bounce.js"></script>
		<script src="js/jquery.stickyheader.js"></script>
	</body>
</html>