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

<body>
    <!-- <h1>Drone Racing Competition - Pilot Registration</h1> -->
    

    <main>
    <div class="container">
    <a class="title-link" href="./index.php"><h1 class="title-text">EMU Drone Racing Competition</h1></a>
    <div class="container">
        <form class="form" action="wait.php" method="POST">

        <h2>Pilot Info</h2>
        <div class="field">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </div>
        
        <br>

        <div class="field">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        </div>
        

        <br>
        <input type="submit" value="Register and Fly">
            </form>
        </div>
    </div>
    </main>
    
</body>

</html>