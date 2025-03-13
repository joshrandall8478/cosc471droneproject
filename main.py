from codrone_edu.drone import *
from stopwatch import Stopwatch
from time import sleep
from database import Leaderboard
from database import Pilot

# import GUI
import tkinter as tk
gui = tk.Tk()
gui.geometry("600x400")

import os

global stopwatch 
global name
global email

stopwatch = Stopwatch(2)

# drone = Drone()
# drone.pair() # To pair automatically, may not always work

global colorSeq
colorSeq = ["Green", "Blue", "Red"] # Will be an environment variable later

global colorActive

def clear():
 
    # for windows, os.name is 'nt'
    if os.name == "nt":
        os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

def airborne():
    if "ModeFlight.Flight" in str(drone.get_flight_state()) or "ModeFlight.TakeOff" in str(drone.get_flight_state()):
        return True
    else:
        return False
    
def runColorSequence():
    stopwatch.reset()
    stopwatch.start()
    print("Getting data...")
    count = 1
    while count <= len(colorSeq):
        print("\nPress the power button on the controller to switch to flight.\nMake sure it shows the navigation arrow.\n")
        time.sleep(1)
        print("Taking off...")
        # drone.takeoff()
        print("Flying...")
        time.sleep(3)
        while airborne():
            None
        print("\nPress the power button on the controller to scan the color.\nMake sure it says LINK.\n")
        time.sleep(2)
        print("Scanning...")
        time.sleep(2)
        # frontColor = drone.get_front_color()
        # backColor = drone.get_back_color()
        colorValid = False
        # print(frontColor)
        # print(backColor)
        # if frontColor is colorSeq[count-1] or backColor is colorSeq[count-1]:
        #     print("Valid Color")
        #     count += 1
        #     colorValid = True
        #     continue
        if not colorValid:
            print("Not a valid color was landed on in sequence")
            return False
    print("Color Sequence Completed")
    return True
    

def loadGUI():
    gui.title('Drone Competition')
    header = tk.Label(gui, text="Welcome to the Drone Competition Program!", font=("Arial", 32))
    header.pack()

    
    button = tk.Button(gui, text='Start Pilot', width=25, command=gui.destroy)
    button.pack()

def main():
    clear()
    # print("Welcome to The Drone Competition Program")
    loadGUI()
    


    name = input("Please enter your name: ")
    email = input("Please enter your email: ")

    database = Pilot("localhost", "droneuser", "dronepassword", "drone", "pilots")
    if database.selectAll("email",email) == None:
        print("User registered!")
        database.insert(name, email)

    pilotId = database.select("pilotId","email",email)[0]
    print()


    
    print("Color sequence:")
    print(colorSeq)
    # print("You will have to press the power button on the drone controller to switch modes for color scanning.\n Follow console instructions.")

    success = runColorSequence()
    stopwatch.stop()

    if success:
        print("Duration: " + str(stopwatch))
        print("Inserting run data into leaderboards...")
        database = Leaderboard("localhost", "droneuser", "dronepassword", "drone", "leaderboard")
        stopwatchResult = '{:.2f}'.format(stopwatch.duration)
        print("Time: " + str(stopwatchResult))
        database.insert(stopwatchResult, pilotId)
    else:
        print("Run is incomplete. To submit a run to the leaderboards, it must be successful.")

    print("Thank you for using The Drone Competition")
    input("Press return to run again")


while True:
    main()