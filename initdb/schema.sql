-- CREATE TABLE dronestats (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     maxHeight INT,
--     maxTemperature FLOAT,
--     maxAccel FLOAT,
--     duration FLOAT
-- )

USE drone;

CREATE TABLE pilots (
    pilotID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE leaderboard (
    runID INT AUTO_INCREMENT PRIMARY KEY,
    duration FLOAT NOT NULL,
    pilotID INT NOT NULL,
    FOREIGN KEY (pilotID) REFERENCES pilots(pilotID)
);