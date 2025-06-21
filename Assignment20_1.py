# Design automation script which accept directory name and display checksum of all files.

# Usage: DirectoryChecksum.py "Demo"
# Demo is name of directory.

import os
import sys
import hashlib

def CheckSum(fname):

    hobj = hashlib.md5()

    fobj = open(fname, 'rb')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)
    
    return hobj.hexdigest()

def DisplayFileInfo(Dir):

    if(os.path.exists(Dir) == False):
        print("No such directory present")
        exit()

    if(os.path.isdir(Dir) == False):
        print("Given input is not a direcctory")
        exit()

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)

    for FolderName, SubFolderNames, FileNames in os.walk(Dir):

        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            ChkSum = CheckSum(fname)

            print("File name :", fname)
            print("CheckSum :", ChkSum, end = "\n\n")

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to display checksum of all the files in the directory")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName") 
            print("Plz provide valid absolute path") 
        else:
            DirName = sys.argv[1]

            DisplayFileInfo(DirName)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
