from codrone_edu.drone import *
from time import sleep

global drone
drone = Drone()
drone.pair()

colorSeq = ["Green", "Blue", "Red"]

global colorActive

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False
    

print(drone.get_colors())

global count
count = 1
print(colorSeq)
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