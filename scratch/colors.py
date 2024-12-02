from codrone_edu.drone import *
from time import sleep
from stopwatch import Stopwatch
from database import Database

# Define global variables, and connect drone object
global drone
global stopwatch

stopwatch = Stopwatch(2)
drone = Drone()
drone.pair()

global colorSeq
colorSeq = ["Green", "Blue", "Red"] # Will be an environment variable later

global colorActive

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False
    

print(drone.get_colors())

global count
count = 1
print("Color sequence: " + colorSeq)

def main():
    stopwatch.start()
    while count <= 3:
        drone.takeoff()
        print("Flying...")
        time.sleep(4)
        while airborne():
            None
        print("Scanning...")
        time.sleep(4)
        frontColor = drone.get_front_color()
        backColor = drone.get_back_color()
        colorValid = False
        print(frontColor)
        print(backColor)
        if frontColor is colorSeq[count-1] or backColor is colorSeq[count-1]:
            print("Valid Color")
            count += 1
            colorValid = True
            continue
        if not colorValid:
            print("Not a valid color was landed on in sequence")
            quit()
    print("Color Sequence Completed")


main()