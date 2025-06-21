# Schedule a function that performs file backup every hour and writes 
# a log entry into backup log.txt.

import schedule
import datetime
import time
import os

def copyContents(srcfile, destFile):

    sobj = open(srcfile, 'r')
    dobj = open(destFile, 'w')

    data = sobj.read(1024)

    while(len(data) > 0):
        dobj.write(data)
        data = sobj.read(1024)
    
    sobj.close()
    dobj.close()
    
def CreateFileName(fname):

    timestamp = time.ctime()

    timestamp = timestamp.replace(' ', '_')
    timestamp = timestamp.replace(':', "__")

    name, ext = os.path.splitext(fname)

    RELname = f"{name}_{timestamp}{ext}"

    folderName = "BackupX"

    if (os.path.exists(folderName) == False):
        os.mkdir(folderName)

    ABSname = os.path.join(os.path.abspath(folderName) , RELname)

    return ABSname, RELname

def CreateLogFile(nfile):

    fobj = open("log.txt", 'a')

    fobj.write("Backup file created with name : " + str(nfile) + "\n")
    fobj.write("Time of creation : " + str(time.ctime()))
    fobj.write("\n\n")

    fobj.close()

def BackupX(fname = "Marvellous.txt"):

    if (os.path.exists(fname) == False):
        print("No such file present")
    
    if (os.path.isfile(fname) == False):
        print("Given input is not a file")

    ABSname, RELname = CreateFileName(fname)

    copyContents(fname, ABSname)

    CreateLogFile(RELname)

    print(f"Successfuly created backup file with {RELname} and enterd log in log.txt")

def main():

    print("Inside main function")
    print("Current time : ")

    schedule.every(1).hour.do(BackupX)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
