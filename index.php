<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drone Racing Competition - Register and View Leaderboard</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <h1>Drone Racing Competition - Pilot Registration</h1>


    <!-- User Registration Form -->
    <form action="register.php" method="POST">
        <label for="name">Pilot Name:</label>
        <input type="text" id="name" name="name" required>


        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>


        <input type="submit" value="Register">
    </form>


    <h2>Leaderboard</h2>




    <table id="data-table">
        <thead>
            <tr>
                <th>Pilot Name</th>
                <th>Email</th>
                <th>Flight Time (seconds)</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Include the database connection
            // include 'connect.php';


            // Fetch data from 'pilots' table
            $db = mysqli_connect("localhost:3306", "droneuser", "dronepassword", "DroneCompetition");  // Connects to database in mysql
            $query = "SELECT * FROM Runs";
            $result = mysqli_query($db,$query);
            $rows = mysqli_num_rows($result);   // Number of rows in $result


            // Check if the query returned any results
            if ($result && $result->num_rows > 0) {
                // Loop through each row and output the data into the table
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['name']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['email']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['flight_time']) . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='3'>No data available</td></tr>";
            }


            // Close connection
            $conn->close();
            ?>
        </tbody>
    </table>
</body>

</html>