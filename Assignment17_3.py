# Write a program that schedules a function to print "Do Coding..!" 
# every 30 minutes.


import schedule
import time
import datetime

def Display():

    print("Do Coding..!")

def main():

    print("Inside main function")
    print("Current time : ", time.ctime())
    
    schedule.every(30).minutes.do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
