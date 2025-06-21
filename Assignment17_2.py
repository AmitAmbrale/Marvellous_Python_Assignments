# Schedule a task that displays the current date and time every 
# minute using the datetime module.

import schedule
import datetime
import time

def DisplayDateTime():

    datetimeX = str(datetime.datetime.now())

    datetimeX = datetimeX.split()

    print("Date :", datetimeX[0])
    print("Time :", datetimeX[1],end="\n\n")

def main():

    print("Inside main function")

    schedule.every(1).minute.do(DisplayDateTime)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
