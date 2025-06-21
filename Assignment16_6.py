# Write a Python program to copy the contents of one file (source.txt) 
# into another file (destination.txt).

import os
import sys

def copyContents(srcFile,destFile):

    if (os.path.exists(srcFile) == False or os.path.exists(destFile) == False):
        print("No such file present")
    
    if (os.path.exists(srcFile)  == False or os.path.exists(destFile)  == False):
        print("Given input is not a file")

    sobj = open(srcFile, 'r')

    dobj = open(file=destFile, mode='a')

    data = sobj.read(1024)

    while(len(data) > 0):
        dobj.write(data)
        data = sobj.read(1024)
    
    sobj.close()
    dobj.close()

def main():

    if(len(sys.argv) == 2):

        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This is used to copy contents from a file to another file")
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  SrcFile.txt DestFile.txt") 
            print("Plz provide valid absolute path")  
    elif (len(sys.argv) == 3): 
        srcFile = sys.argv[1]
        destFile = sys.argv[2]
        copyContents(srcFile, destFile)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()

