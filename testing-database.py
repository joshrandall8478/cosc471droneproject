# from codrone_edu.drone import *
from stopwatch import Stopwatch
from database import Entry, create_connection, setup_database

from time import sleep

# Try to import real Drone, otherwise use MockDrone

global stopwatch 


stopwatch = Stopwatch()
stopwatch.start()
sleep(2)
stopwatch.stop()

# print(stopwatch)
# print('{:.2f}'.format(stopwatch.duration))


exit()



# Establish a database connection
connection = create_connection()
if connection:
    # Set up the database and table if they don’t exist
    setup_database(connection)
    
    # Insert data from drone
    # i leave the mock data there for max_temp and max_speed
    entry = Entry(max_height=45, max_temperature=32.5, max_speed=3.6, duration='{:.2f}'.format(stopwatch.duration))
    entry.insert(connection)
    
    # Close the connection
    connection.close()


# while True:
#     print(drone.get_flight_state())





# drone.land()


# drone.dclose()
