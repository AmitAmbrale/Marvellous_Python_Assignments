# Create a task that runs once every day at 9:00 AM and prints "Namskar..."

import schedule
import time
import datetime

def Display():

    print("Namaskar...")

def main():

    print("Inside main function")
    print("Current time : ", time.ctime())
    
    schedule.every().day.at("09:00").do(Display)

    while(True):
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == '__main__':
    main()
