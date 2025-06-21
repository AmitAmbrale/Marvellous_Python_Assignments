# Design automation script which accept directory name and two file extensions from user. 
# Rename all files with first file extension with the second file extenntion.
# Usage: DirectoryRename.py "Demo" ".txt" ".doc"
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.

# After execution this script each .txt file gets renamed as .doc

import sys
import os

def RenameFiles(Dir, extension1, extension2):

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
            if(fname.endswith(extension1)):

                fname = os.path.join(FolderName, fname)
                
                new_name = os.path.splitext(fname)

                new_name = new_name[0] + extension2

                os.rename(fname, new_name)
                
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
        Fname1 = sys.argv[1]
        extension1 = sys.argv[2]
        extension2 = sys.argv[3]
        RenameFiles(Fname1, extension1, extension2)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()
