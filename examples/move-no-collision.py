from codrone_edu.drone import *
import asyncio

drone = Drone()
drone.pair() # To pair automatically, may not always work

drone.takeoff()
# drone.hover(5)
# drone.avoid_wall(10,50)
# drone.flip("back")

# Print y to console
def print_y():
    while True:
        asyncio.sleep(1)
        print(drone.get_pos_y())

# Check y, land drone if close to ground. All distances are in CM.
def check_y():
    while True:
        asyncio.sleep(1)
        if drone.get_pos_y() < 40:
            drone.land()


# Avoid walls
def keep_distance():
    while True:
        drone.keep_distance(60)


print_y()
check_y()

keep_distance()





# drone.land()

drone.close()