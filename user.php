<?php
require_once ("database.php");
class User {
	public $id;
	public $username;
	public $password;
	public $name;
	public $address;
	public $email;
	public $phone;
	public $score;
	public $collegeid;
	public $college;
	public $city;
	public $country;
	public function __construct() {
	}
	public function insert() {
		global $database;
		$database->prepare_statement ( "INSERT INTO user VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,NULL)" );
		if ($database->stmt) {
			$database->stmt->bind_param ( 'ssssssissss', $this->username, $this->password, $this->name, $this->address, $this->email, $this->phone, $this->score, $this->collegeid, $this->college, $this->city, $this->country );
			$flag = $database->execute_statement ();
			if (! $flag) {
				echo "MySQL error: " . $database->mysqli_error ();
				return false;
			} else {
				return true;
			}
		} else {
			echo "MySQL error: " . $database->mysqli_error ();
			return false;
		}
	}
	public static function authenticate($username = "", $password = "") {
		global $database;
		$database->prepare_statement ( "SELECT userid FROM user WHERE username = ? AND password = ?" );
		if ($database->stmt) {
			$database->stmt->bind_param ( 'ss', $username, $password );
			$database->execute_statement ();
			$database->stmt->bind_result ( $i );
			$found = $database->stmt->fetch ();
			$database->stmt->close ();
			return $found ? $i : false;
		} else {
			echo "MySQL error: " . $database->mysqli_error ();
			return false;
		}
	}
	public static function find_by_id($id) {
		global $database;
		$database->prepare_statement ( "SELECT * FROM user WHERE userid = ?" );
		if ($database->stmt) {
			$database->stmt->bind_param ( 'i', $id );
			$database->execute_statement ();
			$database->stmt->bind_result ( $c1, $c2, $c3, $c4, $c5, $c6, $c7, $c8, $c9, $c10, $c11, $c12, $c13 );
			$found = $database->stmt->fetch ();
			$user = new self ();
			$user->id = $c1;
			$user->username = $c2;
			$user->password = $c3;
			$user->name = $c4;
			$user->address = $c5;
			$user->email = $c6;
			$user->phone = $c7;
			$user->score = $c8;
			$user->collegeid = $c9;
			$user->college = $c10;
			$user->city = $c11;
			$user->country = $c12;
			$user->timestamp = $c13;
			
			$database->stmt->close ();
			return $found ? $user : false;
		} else {
			echo "MySQL error: " . $database->mysqli_error ();
			return false;
		}
	}
	public static function show_top() {
		global $database;
		$database->prepare_statement ( "SELECT * FROM user where userid<>1 and userid<>2 and userid<>3 and userid<>4 ORDER BY score desc,username, UNIX_TIMESTAMP(timestamp) " );
		if ($database->stmt) {
			$database->execute_statement ();
			$database->stmt->bind_result ( $c1, $c2, $c3, $c4, $c5, $c6, $c7, $c8, $c9, $c10, $c11, $c12, $c13 );
			$users = array ();
			$ii = 0;
			while ( $database->stmt->fetch () ) {
				$user = new self ();
				$user->id = $c1;
				$user->username = $c2;
				$user->password = $c3;
				$user->name = $c4;
				$user->address = $c5;
				$user->email = $c6;
				$user->phone = $c7;
				$user->score = $c8;
				$user->collegeid = $c9;
				$user->college = $c10;
				$user->city = $c11;
				$user->country = $c12;
				$users [$ii] = $user;
				$ii ++;
			}
			$database->stmt->close ();
			return $users;
		} else {
			echo "MySQL error: " . $database->mysqli_error ();
			return false;
		}
	}
}