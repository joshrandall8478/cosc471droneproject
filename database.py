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



# """
# commands to see if the necessary tables exist
# """

# cursor.execute("show tables like 'drone'")

# # If database drone doesnt exist, then it will return an empty set. 
# if len(cursor) is 0:
#     cursor.execute("CREATE DATABASE drone")

