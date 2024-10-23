from codrone_edu.drone import *

drone = Drone()
drone.pair() # To pair automatically, may not always work

def color_epilepsy():
    while True:
        drone.set_drone_LED(255,0,0, 100)
        drone.set_drone_LED(0,255,0, 100)
        drone.set_drone_LED(0,0,255, 100)

def regular_epilepsy():
    while True:
        drone.set_drone_LED(255,255,255, 100)
        drone.set_drone_LED(255,255,255, 0)


regular_epilepsy()

# drone.keep_distance(60)

# drone.land()

drone.close()