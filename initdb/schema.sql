-- CREATE TABLE dronestats (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     maxHeight INT,
--     maxTemperature FLOAT,
--     maxAccel FLOAT,
--     duration FLOAT
-- )

USE drone;

CREATE TABLE pilots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE leaderboard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    duration FLOAT,
    pilotID INT,
    FOREIGN KEY (pilotID) REFERENCES pilots(id)
);