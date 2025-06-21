# Design automation script which accept directory name and delete all duplicate 
# files from that directory. Write names of duplicate files from that directory 
# into log file named as Log.txt.

# Log.txt file should be created into current directory.

# Usage: Directory Dusplicate Removal.py "Demo"

# Demo is name of directory.

import sys
import os
import hashlib
import time

def CheckSum(fname):

    hobj = hashlib.md5()

    fobj = open(fname, 'rb')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    return hobj.hexdigest()

def WriteDuplicates(Dir):

    if(os.path.exists(Dir) == False):
        print("No such directory present")
        exit()

    if(os.path.isdir(Dir) == False):
        print("Given input is not a direcctory")
        exit()

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)
    
    Dict = {}

    for FolderName, SubFolderNames, FileNames in os.walk(Dir):

        for fname in FileNames:
            
            fname = os.path.join(FolderName, fname)
            ChkSum = CheckSum(fname)

            if(ChkSum in Dict):
                Dict[ChkSum].append(fname)
            else:
                Dict[ChkSum] = [fname]
    
    return Dict

def createLogFile(Data):

    fobj = open("log.txt", 'a')

    Border = '-'*83

    fobj.write(Border + "\n")
    fobj.write("This is a log file of MARVELLOUS AUTOMATION SCRIPT\n")
    fobj.write(Border + "\n")

    fobj.write("\nTotal number deleted files :" + str(len(Data)))
    fobj.write("\nDeleted Files :\n")

    for value in Data:
        fobj.write(value)
        fobj.write("\n")

    fobj.write("\n")
    fobj.write(Border + "\n")
    fobj.write("This file is created at \n" + str(time.ctime()) + "\n")
    fobj.write(Border + "\n")

    fobj.close()

def listDuplicates(Dir):

    Dict = WriteDuplicates(Dir)

    List = []

    for values in Dict.values():

        for v in range(1, len(values)):
            List.append(values[v])

    deleteFiles(List)
    createLogFile(List)

def deleteFiles(List):

    for value in List:
        os.remove(value)

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to delete duplicate files from given directory & Write names of duplicate files from that directory into log file named as log.txt")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName") 
            print("Plz provide valid absolute path") 
        else:
            DirName = sys.argv[1]
            listDuplicates(DirName)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
