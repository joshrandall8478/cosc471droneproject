<!-- connect.php -->
<?php
// Database connection credentials
$db_server = "localhost:3306";
$db_user = "droneuser";
$db_pass = "dronepassword";
$db_name = "DroneCompetition";
// $conn = "";


// Create connection
$conn = new mysqli($db_server, $db_user, $db_pass, $db_name);


// Check connection
if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}
?>


