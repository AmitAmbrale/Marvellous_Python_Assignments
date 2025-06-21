# Write a Python script that prints "Jay Ganesh..." every 2 seconds. 
# Use the schedule.every(2).seconds.do(...) function.

import schedule
import time
import datetime

def Display():

    print("Jay Ganesh...")

def main():

    print("Inside main function")
    print("Current time : ", time.ctime())
    
    schedule.every(2).seconds.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
