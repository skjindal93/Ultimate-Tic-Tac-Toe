<?php

class Session {
	private $logged_in = false;
	public $user_id;
	function __construct() {
		
		$this->check_login ();
	}
	public function is_logged_in() {
		return $this->logged_in;
	}
	public function login($userid) {
		// database should find user based on username/password
		if ($userid) {
			$this->user_id = $_SESSION ['user_id'] = $userid;
			$this->logged_in = true;
		}
	}
	public function logout() {
		unset ( $_SESSION ['user_id'] );
		unset ( $this->user_id );
		$this->logged_in = false;
	}
	private function check_login() {
		if (isset ( $_SESSION ['user_id'] )) {
			$this->user_id = $_SESSION ['user_id'];
			$this->logged_in = true;
		} else {
			unset ( $this->user_id );
			$this->logged_in = false;
		}
	}
}

$session = new Session();

?>