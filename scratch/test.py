from codrone_edu.drone import *
from stopwatch import Stopwatch
from time import sleep
from database import Leaderboard
from database import Pilot


global stopwatch 
global name
global email

stopwatch = Stopwatch(2)

def main():
    stopwatch.reset()
    print("Welcome to The Drone Competition Program")
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")

    database = Pilot("localhost", "droneuser", "dronepassword", "drone", "pilots")
    if database.selectAll("email",email) == None:
        print("User registered!")
        database.insert(name, email)

    pilotId = database.select("pilotId","email",email)[0]
    print(pilotId)
    stopwatch.start()
    input("Stopwatch started, press return to stop it.")
    stopwatch.stop()
    print("Stopwatch stopped.")

    database = Leaderboard("localhost", "droneuser", "dronepassword", "drone", "leaderboard")
    stopwatchResult = '{:.2f}'.format(stopwatch.duration)
    database.insert(stopwatchResult, pilotId)

main()