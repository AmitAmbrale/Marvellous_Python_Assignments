# Write a program which accept two file names from user and compare contents of both 
# the files. If both the files contains same contents then display success otherwise
# display failure. Accept names of both the files from command line.

# Input: Demo.txt Hello.txt

# Compare contents of Demo.txt and Hello.txt

import sys
import os
import hashlib

def CheckSum(fname):

    hobj = hashlib.md5()

    fobj = open(fname, 'rb')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    return hobj.hexdigest()

def CompareContents(file1, file2):

    if (os.path.exists(file1) == False or os.path.exists(file2) == False):
        print("No such file present")
        exit()
    
    if (os.path.isfile(file1) == False or os.path.isfile(file2) == False):
        print("No such file present")
        exit()

    if (os.path.isabs(file1) == False):
        file1 = os.path.abspath(file1)
    
    if (os.path.isabs(file2) == False):
        file2 = os.path.abspath(file2)

    chkSum1 = CheckSum(file1)
    chkSum2 = CheckSum(file2)

    if(chkSum1 == chkSum2):
        return True
    else:
        return False

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This is used to compare contents of two files")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirectory") 
            print("Plz provide valid absolute path")  
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")
    elif (len(sys.argv) == 3):
        Fname1 = sys.argv[1]
        Fname2 = sys.argv[2]

        ret = CompareContents(Fname1, Fname2)

        if(ret == True):
            print("Success")
        else:
            print("Failure")
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
