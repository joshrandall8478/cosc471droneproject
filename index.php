<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EMU Drone Racing Competition</title>
    <link rel="stylesheet" href="styles.css">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
</head>


<body class="blur background">
    <!-- <h1>Drone Racing Competition - Pilot Registration</h1> -->


    <!-- User Registration Form -->
    <!-- <form action="register.php" method="POST">
        <label for="name">Pilot Name:</label>
        <input type="text" id="name" name="name" required>


        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>


        <input type="submit" value="Register">
    </form> -->

    <main >
    <div class="container">
    <h1 class="title-text">EMU Drone Racing Competition</h1>
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
            // Load environment variables from .env file

            // Fetch data from 'pilots' table
            $db_host = getenv('DB_HOST');
            $db_user = getenv('MYSQL_USER');
            $db_password = getenv('MYSQL_PASSWORD');
            $db_name = getenv('MYSQL_DATABASE');
            $db_port = getenv('DB_PORT');


            // Set default values if environment variables are not set
            $db_host = $db_host ?: 'localhost';
            $db_user = $db_user ?: 'droneuser';
            $db_password = $db_password ?: "dronepassword";
            $db_name = $db_name ?: 'drone';
            $db_port = $db_port ?: '3306';
            
            // echo "<script>console.log('DB_HOST: " . $db_host . "');</script>";
            // echo "<script>console.log('MYSQL_USER: " . $db_user . "');</script>";
            // echo "<script>console.log('MYSQL_PASSWORD: " . $db_password . "');</script>";
            // echo "<script>console.log('MYSQL_DATABASE: " . $db_name . "');</script>";
            // echo "<script>console.log('DB_PORT: " . $db_port . "');</script>";
            $db = mysqli_connect($db_host, $db_user, $db_password, $db_name, $db_port);  // Connects to database in mysql
            if (!$db) {
                die("Connection failed: " . mysqli_connect_error());
            }
            $query = "SELECT P.pilotID, P.name, L.duration from pilots P inner join leaderboard L on L.pilotID = P.pilotID order by L.duration ASC;";
            $result = mysqli_query($db,$query);
            $rows = mysqli_num_rows($result);   // Number of rows in $result

            
            // Check if the query returned any results
            if ($rows > 0) {
                // (ID int, MaxHeightCM float, MaxTemperature float, maxAccel float, Duration float, primary key(id));
                echo "<tr><td>Placement</td><td>Pilot ID</td><td>Name</td><td>Duration</td></tr>";
                // Loop through each row and output the data into the table
                for($i = 0; $i < $rows && $i < 10; $i++){
                    $run = mysqli_fetch_assoc($result);

                    $id = $run["pilotID"];
                    $name = $run["name"];
                    $duration = $run["duration"];
                    $placement = $i + 1;

                    echo "<tr>";
                    echo "<td>$placement</td>";
                    echo "<td>$id</td>";
                    echo "<td>$name</td>";
                    echo "<td>$duration</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='3'>No data available</td></tr>";
            }

            ?>
        <!-- </tbody> -->
    </table>
        
    </div>
    </main>
</body>

</html>