import mysql.connector
from mysql.connector import Error

# Class representing a database entry for a drone flight record
class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        def create_connection(host, user, password, database):
          try:
              connection = mysql.connector.connect(
                  host = host,
                  user = user,
                  password = password,
                  database= database
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
        # def setup_database(connection):
        #     cursor = connection.cursor(buffered=True)
        #     cursor.execute("SHOW DATABASES LIKE" + "'" + database + "'")
        #     if cursor.rowcount == 0:
        #         cursor.execute("CREATE DATABASE " + database)
        #     cursor.execute("USE " + database)
            
        #     # Create the dronestats table if it does not exist
        #     cursor.execute("SHOW TABLES LIKE 'dronestats'")
        #     if cursor.rowcount == 0:
        #         cursor.execute("""
        #             CREATE TABLE dronestats (
        #                 ID INT AUTO_INCREMENT PRIMARY KEY,
        #                 maxHeight INT,
        #                 maxTemperature FLOAT,
        #                 maxAccel FLOAT,
        #                 duration FLOAT
        #             )
        #         """)
        # setup_database(self.connection)
          # Method to insert a new record into the database
    def insert():
       raise NotImplementedError("Must be implemented in a subclass")
    def close(self):
      self.connection.close()

      
# Subclasses
class Leaderboard(Database):
    def __init__(self, host, user, password, database, table):
        super().__init__(host, user, password, database)
        self.table = table
    def insert(self, duration, pilotID):
        try:
            cursor = self.connection.cursor(buffered=True)
            query = f"insert into {self.table} (duration, pilotID) values (%s,%s)"
            values = (duration, pilotID)
            cursor.execute("USE " + self.database)
            cursor.execute(query, values)
            self.connection.commit()
            # print("Drone data inserted successfully.")
        except Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()


class Pilot(Database):
    def __init__(self, host, user, password, database, table):
            super().__init__(host, user, password, database)
            self.table = table
    def insert(self, name, email):
        try:
            cursor = self.connection.cursor(buffered=True)
            query = f"INSERT INTO {self.table} (name, email) VALUES (%s, %s)"
            values = (name, email)
            cursor.execute("USE " + self.database)
            cursor.execute(query, values)
            self.connection.commit()
            # print("Drone data inserted successfully.")
        except Error as e:
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()
    def selectAll(self, attribute, val):
        try:
            cursor = self.connection.cursor(buffered=True)
            query = f"select * from {self.table} where {attribute} = %s"
            values = (val,)
            cursor.execute("USE " + self.database)
            cursor.execute(query, values)
            result = cursor.fetchone()
            return result
        except Error as e:
            print(f"Failed to retrieve data: {e}")
        finally:
            cursor.close()
    
    def select(self, selected, attribute, val):
        try:
            cursor = self.connection.cursor(buffered=True)
            query = f"select {selected} from {self.table} where {attribute} = %s"
            values = (val,)
            cursor.execute("USE " + self.database)
            cursor.execute(query, values)
            result = cursor.fetchone()
            # print("Drone data inserted successfully.")
            return result
        except Error as e:
            print(f"Failed to retrieve data: {e}")
        finally:
            cursor.close()