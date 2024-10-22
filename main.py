from codrone_edu.drone import *

drone = Drone()
drone.pair() # To pair automatically, may not always work

drone.takeoff()
# drone.hover(5)
# drone.avoid_wall(10,50)
# drone.flip("back")

drone.keep_distance(60)

# drone.land()

drone.close()