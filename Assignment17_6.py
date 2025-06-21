# Write a script that schedules multiple tasks: one to print "Lunch Time!" 
# at 1 PM, and another to print "Wrap up work" at 6 PM.

import schedule
import time
import datetime

def LunchTime():

    print("Lunch Time!")

def WrapUp():

    print("Wrap up work")
    
def main():

    print("Inside main function")
    print("Current time : ", time.ctime())
    
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUp)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()