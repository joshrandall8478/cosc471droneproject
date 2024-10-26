import mysql.connector
from mysql.connector import Error

# Class representing a database entry for a drone flight record
class Database:
    def __init__(self, host, user,password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        def create_connection(host, user,password, database):
          try:
              connection = mysql.connector.connect(
                  host = host,
                  user = user,
                  password = password,
                  datbase= database
                  # host="localhost",
                  # user="droneuser",
                  # password="dronepassword",
                  # database="drone"
              )
              if connection.is_connected():
                  print("Connected to the database successfully.")
              return connection
          except Error as e:
              print(f"Error connecting to the database: {e}")
              return None
        self.connection = create_connection(self.host, self.user, self.password, self.database)
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
        setup_database(self.connection)
          # Method to insert a new record into the database
    def insert(self, max_height, max_temperature, max_speed, duration):
        try:
            cursor = self.connection.cursor(buffered=True)
            query = """
                INSERT INTO dronestats (id, maxHeight, maxTemperature, maxSpeed, duration)
                VALUES (%s, %s, %s, %s)
            """
            values = (max_height, max_temperature, max_speed, duration)
            cursor.execute("USE drone")
            cursor.execute(query, values)
            self.connection.commit()
            print("Drone data inserted successfully.")
        except Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()
    def close(self):
      self.connection.close()

                # Function to create a connection to the MySQL database
    

    
