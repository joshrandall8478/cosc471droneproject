from codrone_edu.drone import *
from stopwatch import Stopwatch
from time import sleep
from database import Leaderboard
from database import Pilot

# import GUI
import tkinter as tk
gui = tk.Tk()
gui.geometry("800x600")

current_frame = None

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

def switch_frame(new_frame):
    global current_frame  # Access the global variable
    if current_frame is not None:
        current_frame.destroy()  # Destroy the current frame if it exists
    current_frame = new_frame  # Set the new frame as the current frame
    current_frame.pack(fill="both", expand=True)  # Display the new frame

def start_page():
    start_frame = tk.Frame(gui)
    header = tk.Label(start_frame, text="Welcome to the Drone Competition Program!", font=("Arial", 32))
    header.grid(row=0, column=0,padx=10, pady=80,sticky="n")
    button = tk.Button(start_frame, text='Start Pilot',font=("Arial", 20), command=lambda: switch_frame(registration_page()))
    button.grid(row=1,column=0,padx=10, pady=10,sticky="n")

    # Center the frame in the window
    start_frame.grid_rowconfigure(0, weight=0)  # Make the first row not stretchable
    start_frame.grid_rowconfigure(1, weight=0)  # Make the second row not stretchable
    start_frame.grid_columnconfigure(0, weight=1)  # Make the column stretchable
    return start_frame

def registration_page():
    registration_frame = tk.Frame(gui)

    # Create and configure header label
    header = tk.Label(registration_frame, text="Registration", font=("Arial", 32))
    header.grid(row=0, column=0, columnspan=2, pady=20, sticky="n") 

    # Username label and input field
    name_label = tk.Label(registration_frame, text="Username", font=("Arial", 24))
    name_label.grid(row=1, column=0, sticky="e", padx=10)  # Align text to the right of the column
    name_field = tk.Text(registration_frame, height=1, font=("Arial", 24))
    name_field.grid(row=1, column=1, sticky="ew", padx=10)  # Align text box to the left of the column

    # Password label and input field
    email_label = tk.Label(registration_frame, text="Password", font=("Arial", 24))
    email_label.grid(row=2, column=0, sticky="e", padx=10)  # Align text to the right of the column
    email_field = tk.Text(registration_frame, height=1, font=("Arial", 24))
    email_field.grid(row=2, column=1, sticky="ew", padx=10)  # Align text box to the left of the column

    # Register button with column span
    button = tk.Button(registration_frame, text='Register', font=("Arial", 20), command=lambda: switch_frame(start_flight_page()))
    button.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")  # Center the button, no horizontal stretch

    # Set the first column to fit the content
    registration_frame.grid_columnconfigure(0, weight=0)
    # Set the second column to be stretchable
    registration_frame.grid_columnconfigure(1, weight=1) 

    return registration_frame

def start_flight_page():
    start_flight_frame = tk.Frame(gui)
    return start_flight_frame

def flight_page():
    flight_frame = tk.Frame(gui)
    return flight_frame

def result_page():
    result_frame = tk.Frame(gui)
    return result_frame

def end_page():
    end_frame = tk.Frame(gui)
    return end_frame
    

def main():
    clear()
    # print("Welcome to The Drone Competition Program")
    switch_frame(start_page())



    gui.title('Drone Competition')

    


    # registration_frame = tk.Frame(gui)
    # registration_frame.pack()


    # start_flight_frame = tk.Frame(gui)
    # start_flight_frame.pack()


    gui.mainloop()
    


    # name = input("Please enter your name: ")
    # email = input("Please enter your email: ")

    # database = Pilot("localhost", "droneuser", "dronepassword", "drone", "pilots")
    # if database.selectAll("email",email) == None:
    #     print("User registered!")
    #     database.insert(name, email)

    # pilotId = database.select("pilotId","email",email)[0]
    # print()


    
    # print("Color sequence:")
    # print(colorSeq)
    # # print("You will have to press the power button on the drone controller to switch modes for color scanning.\n Follow console instructions.")

    # success = runColorSequence()
    # stopwatch.stop()

    # if success:
    #     print("Duration: " + str(stopwatch))
    #     print("Inserting run data into leaderboards...")
    #     database = Leaderboard("localhost", "droneuser", "dronepassword", "drone", "leaderboard")
    #     stopwatchResult = '{:.2f}'.format(stopwatch.duration)
    #     print("Time: " + str(stopwatchResult))
    #     database.insert(stopwatchResult, pilotId)
    # else:
    #     print("Run is incomplete. To submit a run to the leaderboards, it must be successful.")

    # print("Thank you for using The Drone Competition")
    # input("Press return to run again")


while True:
    main()