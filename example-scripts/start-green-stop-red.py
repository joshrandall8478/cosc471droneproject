from codrone_edu.drone import *

drone = Drone()
drone.pair() # To pair automatically, may not always work

global scannedColors



def isRed(colors):
    sleep(1)
    print(colors)
    if colors[0] == 'Green' and colors[1] == 'Green':
        return True
    else:
        return False
# while True:
#     scannedColors = drone.get_colors()
#     print(scannedColors)
    
# calibrate()
# loadData()
# drone.new_color_data(color, data, dataset)
while True:
    sleep(1)
    scannedColors = drone.get_colors()
    print(scannedColors)
    if scannedColors[0] == 'Black' and scannedColors[1] == 'Black':
        drone.takeoff()
        drone.set_throttle(-20)
        print("Moving down")
        drone.move(1)
        drone.reset_move()

        scannedColors = drone.get_colors()

        while not isRed(scannedColors):
            drone.set_pitch(50)
            print("Moving forward")
            drone.move(2)
            drone.reset_move()



            while drone.get_height() >= 20:
                drone.set_throttle(-20)
                print("Moving Down")
                drone.move(1)
                drone.reset_move()


            print("Getting colors")
            scannedColors=drone.get_colors()
            print(scannedColors)
    

            if isRed(scannedColors):
                print("Landing")
                drone.land()
            else:
                while drone.get_height() < 30:
                    drone.set_throttle(40)
                    print("Moving Up")
                    drone.move(2)
                    drone.reset_move()




drone.close()