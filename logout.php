<?php
require_once ("header.php");

if (!$session->is_logged_in ()) {
	require_once ("header.php");
	//echo ("You're already logged out!"."\n");
}
else {
	$session->logout();
	require_once ("header.php");
	//echo ("Logged out successfully!"."\n");
	printf ( "<script>location.href='index.php'</script>" );
}
?>