import mysql.connector




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass123",
  database="drone"
)

print(mydb) # test to see if connection was successful

cursor = mydb.cursor(buffered=True)
cursor.execute()
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
                maxHeight INT,
                maxTemperature FLOAT,
                maxSpeed FLOAT,
                duration FLOAT
            )
        """)
    cursor.close()

class Entry:
  def __init__(self, maxHeight, temperature, speed, duration):
    self.maxHeight = maxHeight
    self.temp = temperature
    self.speed = speed
    self.duration = duration

  
  def insert(self, connection):
    try:
      cursor = connection.cursor()
      query = """
          INSERT INTO dronestats (max_height, temperature, speed, duration)
          VALUES (%s, %s, %s, %s)
      """
      values = (self.max_height, self.temperature, self.speed, self.duration)
      cursor.execute(query, values)
      connection.commit()
      print("Drone data inserted successfully.")
    except Error as e:
        print(f"Failed to insert data: {e}")
    finally:
        cursor.close()
