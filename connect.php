<!-- connect.php -->
<?php
// Database connection credentials
$db_server = "127.0.0.1";
$db_user = "root";
$db_pass = "";
$db_name = "businessdb";
$conn = "";


// Create connection
$conn = new mysqli($db_server, $db_user, $db_pass, $db_name);


// Check connection
if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
}
?>


