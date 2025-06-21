# Design automation script which accept directory name from user and create log 
# file in that directory which contains information of running processes as 
# its name, PID, Username.

# Usage: ProcInfoLog.py Demo

# Demo is name of Directory.

import psutil
import os
import time
import sys

def ProcessScan():

    List = []

    for proc in psutil.process_iter():
        info = proc.as_dict(['name', 'pid', 'username'])
        List.append(info)
    
    return List

def CreateLogFile(Dir):

    timestamp = time.ctime()

    fname = "Marvellous_%s.log" %(timestamp)

    fname = fname.replace(" ", "_")
    fname = fname.replace(":", "__")

    Data = ProcessScan()

    if(os.path.exists(Dir) == False):
        os.mkdir(Dir)

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)

    fname = os.path.join(Dir, fname)

    fobj = open(fname, 'w')

    Border = '-'*83

    fobj.write(Border + "\n")
    fobj.write("This is a log file of MARVELLOUS AUTOMATION SCRIPT\n")
    fobj.write(Border + "\n\n")

    fobj.write("Total number of process running : "+ str(len(Data)))
    fobj.write("\nRunning Processes :\n")
    
    for value in Data:
        fobj.write("\n%s\n" %(value))

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("This file is created at \n" + timestamp + "\n")
    fobj.write(Border + "\n")

    print("File created with name ", {fname})

    fobj.close()

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to create log file in given directory which contains information of running processes as its name, PID, Username.")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName") 
            print("Plz provide valid absolute path") 
        else:
            DirName = sys.argv[1]
            CreateLogFile(DirName)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
