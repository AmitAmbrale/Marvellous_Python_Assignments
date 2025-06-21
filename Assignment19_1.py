# Design automation script which accept directory name and file extension from user. 
# Display all files with that extension.
# Usage: DirectoryFileSearch.py "Demo" ".txt"

import sys
import os

def DisplayFiles(Dir, extension):

    if (os.path.exists(Dir) == False):
        print("No such file present")
        exit()

    if (os.path.isdir(Dir) == False):
        print("Given input is not a directory")
        exit()

    if(os.path.isabs(Dir) == False):
        Dir = os.path.abspath(Dir)
    
    for FolderName, SubFolderNames, FileNames in os.walk(Dir):
        
        for fname in FileNames:

            if(fname.endswith(extension)):
                fname = os.path.join(FolderName, fname)
                print(fname)

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to display all files with given extension.")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName extension") 
            print("Plz provide valid absolute path") 
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")
    elif (len(sys.argv) == 3):
        Fname1 = sys.argv[1]
        extension = sys.argv[2]
        DisplayFiles(Fname1, extension)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
