<?php
require_once ("config.php");
class MySQLDatabase {
	private $connection;
	public $stmt;
	function __construct() {
		$this->connection = new mysqli ( DB_SERVER, DB_USER, DB_PASS, DB_NAME );
		if (mysqli_connect_errno ()) {
			die ( "Database Connection Failed: " . mysqli_connect_error () );
		}
	}
	function __destruct() {
		$this->connection->close ();
	}
	public function query($sql) {
		$result = $this->connection->query ( $sql );
		if (! $result) {
			die ( "MySQL Query Failed: " . $this->connection->error );
		}
		return $result;
	}
	public function prepare_statement($sql) {
		$this->stmt = $this->connection->prepare ( $sql );
	}
	public function execute_statement() {
		return $this->stmt->execute ();
	}
	public function mysqli_error() {
		return $this->connection->error;
	}
}

$database = new MySQLDatabase ();

?>