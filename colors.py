from codrone_edu.drone import *

drone = Drone()
drone.pair()

colorSeq = ["Green", "Yellow", "Red"]

global colorActive

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False
    


global count
count = 1
print(colorSeq)
while count != 3:
    drone.takeoff()
    print("Flying...")
    sleep(2)
    while airborne():
        None
    print("Scanning...")
    sleep(1)
    colors = drone.get_colors()
    colorValid = False
    for color in colors:
        print(color)
        if color is colorSeq[count-1]:
            count += 1
            colorValid = True
            break
    if not colorValid:
        print("Not a valid color was landed on in sequence")
        break