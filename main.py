from codrone_edu.drone import *
from stopwatch import Stopwatch
from database import Entry, create_connection, setup_database

global stopwatch 
global max_temperature
global max_speed
global max_height

stopwatch = Stopwatch(2)



drone = Drone()
drone.pair() # To pair automatically, may not always work

# async def print_flight_state():
#     print(drone.get_flight_state())
#     await asyncio.sleep(1)

# global seconds
# seconds = 0
# def count():
#     global seconds
#     while True:
#         seconds = seconds + 1
#         sleep(1)


drone.takeoff()

# asyncio.run(print_flight_state())

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False


# global 
max_height = 0
max_temperature = 0
max_speed = 0

def get_values():
    global max_height
    while airborne():
        print(drone.get_pos_z(unit="cm"))
        if drone.get_pos_y() > max_height:
            max_height = drone.get_pos_z(unit="cm")


stopwatch.start()

while airborne():
    get_values()

stopwatch.stop()

print("Max Height: " + str(max_height) + "cm")
print("Duration: " + str(stopwatch))

# Establish a database connection
connection = create_connection()
if connection:
    # Set up the database and table if they don’t exist
    setup_database(connection)
    
    # Insert data from drone
    # i leave the mock data there for max_temp and max_speed
    entry = Entry(max_height=max_height, max_temperature=max_temperature, max_speed=max_speed, duration='{:.2f}'.format(stopwatch.duration))
    entry.insert(connection)
    
    # Close the connection
    connection.close()


# while True:
#     print(drone.get_flight_state())





# drone.land()


drone.close()