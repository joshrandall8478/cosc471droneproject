from codrone_edu.drone import *
import mysql.connector

drone = Drone()
drone.pair() # To pair automatically, may not always work

drone.takeoff()

# Print y to console
def print_y():
    while True:
        # asyncio.sleep(1)
        print(drone.get_pos_y())



# Avoid walls
def keep_distance():
    while True:
        drone.keep_distance(60)


print_y()

keep_distance()





# drone.land()

drone.close()