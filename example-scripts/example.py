#Python code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()


if drone.detect_wall(50):
    print("wall detected!")
    drone.keep_distance(50)
else:
    print("no wall detected!")

# drone.land()


drone.close()