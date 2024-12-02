from codrone_edu.drone import *
from stopwatch import Stopwatch
from time import sleep
from database import Leaderboard
from database import Pilot

global stopwatch 
global name
global email

stopwatch = Stopwatch(2)

drone = Drone()
drone.pair() # To pair automatically, may not always work

global colorSeq
colorSeq = ["Green", "Blue", "Red"] # Will be an environment variable later

global colorActive

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False
    
def runColorSequence():
    stopwatch.reset()
    stopwatch.start()
    print("Getting data...")
    while count <= len(colorSeq):
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
            return False
    print("Color Sequence Completed")
    return True
    

def main():
    print("Welcome to The Drone Competition Program")
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")

    database = Pilot("localhost", "droneuser", "dronepassword", "drone", "pilots")
    if database.selectAll("email",email) == None:
        print("User registered!")
        database.insert(name, email)

    pilotId = database.select("pilotId","email",email)[0]
    print()


    global count
    count = 1
    print("Color sequence: " + colorSeq)

    success = runColorSequence()
    stopwatch.stop()
    print("Duration: " + str(stopwatch))

    if success:
        print("Inserting run data into leaderboards...")
        database = Leaderboard("localhost", "droneuser", "dronepassword", "drone", "leaderboard")
        stopwatchResult = '{:.2f}'.format(stopwatch.duration)
        database.insert(stopwatchResult, pilotId)
    else:
        print("Run is incomplete. To submit a run to the leaderboards, it must be successful.")

    print("Thank you for using The Drone Competition")
    input("Press return to run again")

while True():
    main()