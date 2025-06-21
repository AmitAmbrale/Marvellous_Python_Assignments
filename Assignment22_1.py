# Please follow below rules while designing automation script as

# Accept input through command line or through file.

# Display any message in log file instead of console.

# For separate task define separate function.

# For robustness handle every expected exception.

# Perform validations before taking any action.

# Create user defined modules to store the functionality.

# Design automation script which performs following task.

# Accept Directory name from user and delete all duplicate files from the specified 
# directory by considering the checksum of files.

# Create one Directory named as Marvellous and inside that directory create log file 
# which maintains all names of duplicate files which are deleted.

# Name of that log file should contains the date and time at which that file gets created.

# Accept duration in minutes from user and perform task of duplicate file removal 
# after the specific time interval. 

# Accept Mail id from user and send the attachment of the log file.

# Mail body should contains statistics about the operation of duplicate file removal.

# Mail body should contains below things:

# Starting time of scanning Total number of files scanned

# Total number of duplicate files found

# Consider below command line options for the gives script

# Duplicate File Removal.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

# - DuplicateFileRemoval.py

# Name of python automation script

# - E:/Data/Demo

# -50

# Absolute path of directory which may contains duplicate files

# Time interval of script in minutes

# marvellousinfosystem@gmail.com

# Note:

# Mail ID of the receiver

# For every separate task write separate function.

# Write all user defined functions in one user defined module.

# Use proper validation techniques.

# Provide Help and usage option for script.

# Create one Readme file which contains description of our script, details of 
# command line options.

# Design automation script which accept directory name and delete all duplicate 
# files from that directory. Write names of duplicate files from that directory 
# into log file named as Log.txt.

# Log.txt file should be created into current directory.

# Usage: Directory Dusplicate Removal.py "Demo"

# Demo is name of directory.

import sys
import os
import time
import schedule
import email.message as e
from StoreDuplicateFiles import WriteDuplicates
from SENDMAIL import SendMail
from Create_LogFile import createLogFile
from DuplicateFiles import listDuplicates
from VerifyEmail import CheckEmail
from DeleteFiles import deleteFiles

def MySchedule(List):

    DirName = List[0]
    TimeInterval = List[1]
    Email_ID = List[2]
    StartTime = List[3]

    Dict, ScanCount = WriteDuplicates(DirName)
    DupList = listDuplicates(Dict)
    deleteFiles(DupList)
    LogFile = createLogFile(DupList, ScanCount)
    SendMail(LogFile, Email_ID, len(DupList), ScanCount, StartTime)

    print("Successfuly duplicate files deleted & log file (",str(os.path.relpath(LogFile)),") send to :", Email_ID)
    print("Total number of scanned files :", ScanCount)
    print("Total number of deleted files :", len(DupList))

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to delete duplicate files from given directory & Write names of duplicate files from that directory into log file named as log.txt and send that log file to the given email id")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName TimeInterval Email_ID") 
            print("Plz provide valid absolute path") 
    elif (len(sys.argv) == 4):
        List = []             
        start = time.ctime()

        List.append(sys.argv[1])
        List.append(sys.argv[2])
        List.append(sys.argv[3])
        List.append(start)

        CheckEmail(List[2])

        schedule.every(int(List[1])).seconds.do(MySchedule, List)

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
