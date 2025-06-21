# Write a program which accept file name from user and create new file 
# named as Demo.txt and copy all contents from existing file into new file. 
# Accept file name through command line arguments.

# Input: ABC.txt

# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt


import os
import sys

def copyContents(srcFile):

    if(os.path.exists(srcFile) == False):
        print("No such file present")
        exit()

    if(os.path.isfile(srcFile) == False):
        print("Given input is not a file")
        exit()

    if(os.path.isabs(srcFile) == False):
        srcFile = os.path.abspath(srcFile)

    sobj = open(srcFile, 'r')

    dobj = open("Demo.txt", 'w')

    data = sobj.read()

    dobj.write(data)

    print(f"Successfully data copied from {srcFile} to Demo.txt")

    sobj.close()
    dobj.close()

def main():

    if(len(sys.argv) == 2):

        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This is used to copy contents from a existing file into a new file")
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NewFile.txt") 
            print("Plz provide valid absolute path")  
        else: 
            FName = sys.argv[1]
            copyContents(FName)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
