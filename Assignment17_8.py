# Write a script that simulates checking for email updates every 10 seconds. 
# (Use a print statement like "Checking mail..." instead of real email logic.)

import schedule
import time
import datetime

def CheckingMail():

    print("Checking mail...")

def main():

    print("Inside main function ")
    print("Current time :", time.ctime())

    schedule.every(10).seconds.do(CheckingMail)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
