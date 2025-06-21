# Schedule a job that runs every 5 minutes to write the current 
# time to a file Marvellous.txt.

import schedule
import time
import datetime
import os

def WriteTime():

    fname = "Marvellous.txt"
    fobj = None

    # if (os.path.exists(fname) == False):
    #     fobj = open(fname, 'w')
    # else:
    #     fobj = open(fname, 'a')

    fobj = open(fname, 'a')

    timeX = datetime.datetime.now()

    fobj.write("Current time : " + str(timeX))
    fobj.write('\n')

    fobj.close()

    print("Current time written in Marvellous.txt successfully")
    
def main():

    print("Inside main function")
    print("Current time : ", time.ctime())
    
    schedule.every(1).seconds.do(WriteTime)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()