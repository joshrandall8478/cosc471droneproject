from codrone_edu.drone import *
from stopwatch import Stopwatch
from database import Entry, create_connection, setup_database
import asyncio

import database


global stopwatch 

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

global max_height
# global 
max_height = 0

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


# while True:
#     print(drone.get_flight_state())





# drone.land()

drone.close()
conn = create_connection()
if conn:
    setup_database(conn)
    # ! Define drone temperature
    entry = Entry(max_height=max_height, temperature=temperature, speed=speed, duration=stopwatch)
    entry.insert(conn)
    conn.close()