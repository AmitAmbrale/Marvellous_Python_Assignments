# Design automation script which accept two directory names and one file extension. 
# Copy all files with the specified extension from first directory into second directory. 
# Second directory should be created at run time.

# Usage: Directory CopyExt.py "Demo" "Temp" ".exe"

# Demo is name of directory which is existing and contains files in it. 
# We have to create new Directory as Temp and copy all files with extension .exe 
# from Demo to Temp.

import os
import sys
import shutil

def CopyFilesByExtension(Dir1, Dir2, extension):

    if (os.path.exists(Dir1) == False):
        print("No such file present")
        exit()

    if (os.path.isdir(Dir1) == False):
        print("Given input is not a directory")
        exit()

    if(os.path.isabs(Dir1) == False):
        Dir1 = os.path.abspath(Dir1)

    if(os.path.exists(Dir2) == False):
        os.mkdir(Dir2)
    
    if(os.path.isabs(Dir2) == False):
        Dir2 = os.path.abspath(Dir2)

    FolderName = None

    for FolderName, SubFolderNames, FileNames in os.walk(Dir1):
        for fname in FileNames:
            if(fname.endswith(extension)):
                fname = os.path.join(FolderName, fname)
                shutil.copy(fname, Dir2)

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to rename all files with first file extension with the second file extenntion.")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  DirectoryName first_extension second_extension") 
            print("Plz provide valid absolute path") 
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")
    elif (len(sys.argv) == 4):
        Dir1 = sys.argv[1]
        Dir2 = sys.argv[2]
        extension = sys.argv[3]
        CopyFilesByExtension(Dir1, Dir2, extension)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
