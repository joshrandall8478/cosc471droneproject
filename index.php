<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Drone Racing Competition - Register and View Leaderboard</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <!-- <h1>Drone Racing Competition - Pilot Registration</h1> -->


    <!-- User Registration Form -->
    <!-- <form action="register.php" method="POST">
        <label for="name">Pilot Name:</label>
        <input type="text" id="name" name="name" required>


        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>


        <input type="submit" value="Register">
    </form> -->


    <h1>Drone Stats</h1>




    <table id="data-table">
        <!-- <thead>
            <tr>
                <th>Pilot Name</th>
                <th>Email</th>
                <th>Flight Time (seconds)</th>
            </tr>
        </thead>
        <tbody> -->
            <?php
            // Include the database connection
            // include 'connect.php';


            // Fetch data from 'pilots' table
            $db = mysqli_connect("localhost:3306", "droneuser", "dronepassword", "drone");  // Connects to database in mysql
            $query = "SELECT * FROM dronestats";
            $result = mysqli_query($db,$query);
            $rows = mysqli_num_rows($result);   // Number of rows in $result

            
            // Check if the query returned any results
            if ($rows > 0) {
                // (ID int, MaxHeightCM float, MaxTemperature float, maxAccel float, Duration float, primary key(id));
                echo "<tr><td>ID</td><td>Max Height</td><td>Max Temperature</td><td>Max Accel</td><td>Duration</td></tr>";
                // Loop through each row and output the data into the table
                for($i = 0; $i < $rows; $i++){
                    $run = mysqli_fetch_assoc($result);

                    $id = $run["ID"];
                    $maxHeight = $run["maxHeight"];
                    $maxTemp = $run["maxTemperature"];
                    $maxAccel = $run["maxAccel"];
                    $duration = $run["duration"];

                    echo "<tr>";
                    echo "<td>$id</td>";
                    echo "<td>$maxHeight</td>";
                    echo "<td>$maxTemp</td>";
                    echo "<td>$maxAccel</td>";
                    echo "<td>$duration</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='3'>No data available</td></tr>";
            }

            ?>
        <!-- </tbody> -->
    </table>
</body>

</html>