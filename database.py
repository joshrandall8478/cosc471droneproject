import mysql.connector
from mysql.connector import Error

# Function to create a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="droneuser",
            password="dronepassword",
            database="drone"
        )
        if connection.is_connected():
            print("Connected to the database successfully.")
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

# Function to set up the database and create the required table if not exists
def setup_database(connection):
    cursor = connection.cursor(buffered=True)
    cursor.execute("SHOW DATABASES LIKE 'drone'")
    if cursor.rowcount == 0:
        cursor.execute("CREATE DATABASE drone")
    cursor.execute("USE drone")
    
    # Create the dronestats table if it does not exist
    cursor.execute("SHOW TABLES LIKE 'dronestats'")
    if cursor.rowcount == 0:
        cursor.execute("""
            CREATE TABLE dronestats (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                max_height INT,
                max_temperature FLOAT,
                max_speed FLOAT,
                duration FLOAT
            )
        """)
    cursor.close()

# Class representing a database entry for a drone flight record
class Entry:
    def __init__(self, max_height, max_temperature, max_speed, duration):
        self.max_height = max_height
        self.max_temperature = max_temperature
        self.max_speed = max_speed
        self.duration = duration

    # Method to insert a new record into the database
    def insert(self, connection):
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO dronestats (maxHeight, maxTemperature, maxSpeed, duration)
                VALUES (%s, %s, %s, %s)
            """
            values = (self.max_height, self.max_temperature, self.max_speed, self.duration)
            cursor.execute(query, values)
            connection.commit()
            print("Drone data inserted successfully.")
        except Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()
