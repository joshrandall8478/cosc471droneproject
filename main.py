from codrone_edu.drone import *

drone = Drone()
drone.pair() # To pair automatically, may not always work

drone.takeoff()
drone.hover(1)

drone.land()

drone.close()