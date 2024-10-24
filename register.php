<!-- register.php -->
<?php
// Include the database connection
include 'connect.php';

// Check if the form data is set
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);

    // Insert data into 'pilots' table
    $sql = "INSERT INTO pilots (name, email, flight_time) VALUES (?, ?, 0)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $name, $email);

    if ($stmt->execute()) {
        echo "Registration successful! <a href='index.php'>View Leaderboard</a>";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>
