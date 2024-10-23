<?php
            // Database connection
            $host = "localhost";
            $dbname = "drone_racing";  // Replace with your actual DB name
            $username = "root";
            $password = "";  // Replace with your actual password

            // Create connection
            $conn = new mysqli($host, $username, $password, $dbname);

            // Check connection
            if ($conn->connect_error) {
                die("Connection failed: " . $conn->connect_error);
            }

            // Fetch data from 'pilots' table
            $sql = "SELECT name, email, flight_time FROM pilots";
            $result = $conn->query($sql);

            // Check if the query returned any results
            if ($result->num_rows > 0) {
                // Loop through each row and output the data into the table
                while($row = $result->fetch_assoc()) {
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