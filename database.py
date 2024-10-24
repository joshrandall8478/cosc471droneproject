import mysql.connector




mydb = mysql.connector.connect(
  host="localhost",
  user="droneuser",
  password="dronepassword"
)

print(mydb) # test to see if connection was successful

cursor = mydb.cursor(buffered=True)


"""
commands to see if database exists
"""

cursor.execute("show databases like 'drone'")

# If database drone doesnt exist, then it will return an empty set. 
if cursor.rowcount == 0:
    cursor.execute("CREATE DATABASE drone")

cursor.execute("use drone")


cursor.execute("show tables like 'runs'")

# If database drone doesnt exist, then it will return an empty set. 
if cursor.rowcount == 0:
    cursor.execute("create table Runs ( ID int, MaxHeightCM float, MaxTemperature float, MaxSpeed float, Duration float);")


class Entry:
  def __init__(self, maxHeight, temperature, speed):
    self.maxHeight = maxHeight
    self.temp = temperature
    self.speed = speed
  
  # def insert()
