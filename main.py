from codrone_edu.drone import *
from stopwatch import Stopwatch
from database import Database

global stopwatch 
global max_temperature
global max_accel
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
max_accel = 0

def get_height():
    global max_height
    # print(drone.get_height(unit="cm"))
    if drone.get_pos_z() > max_height:
        max_height = drone.get_pos_z(unit="cm")

def get_temperature():
    global max_temperature
    # print(drone.get_temperature(unit="f"))
    if drone.get_temperature() > max_temperature:
        max_temperature = drone.get_temperature(unit="f")

def get_accel():
    global max_accel
    x = max(drone.get_x_accel(),drone.get_y_accel())
    if x > max_accel:
        max_accel = x


# global totalHeight
# global heightPoints
# totalHeight = 0
# heightPoints = 0
# def computeHeight():
#     global totalHeight
#     global heightPoints
#     totalHeight = totalHeight + drone.get_pos_z(unit="cm")
#     heightPoints = heightPoints + 1

stopwatch.start()

print("Getting data...")
while airborne():
    get_height()
    get_temperature()
    get_accel()

stopwatch.stop()


print("Max Height: " + str(max_height) + "cm")
print("Max Temperature: " + str(max_temperature) + "F")
print("Max Accel: " + str(max_accel) + "mm/s")
print("Duration: " + str(stopwatch))

database = Database("localhost", "droneuser", "dronepassword", "drone")
database.insert(max_height,max_temperature,max_accel,'{:.2f}'.format(stopwatch.duration))

# while True:
#     print(drone.get_flight_state())





# drone.land()


# drone.close()