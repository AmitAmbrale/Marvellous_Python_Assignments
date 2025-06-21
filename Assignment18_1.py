# Write a program which accepts file name from user and check whether that file 
# exists in current directory or not.

# Input : Demo.txt
# Check whether Demo.txt exists or not.

import os

def chkFileExists(FileName):

    return (os.path.exists(FileName) and os.path.isfile(FileName))

def main():
  
    FileName = input("Enter name of file :")

    if(chkFileExists(FileName)):
        print("File exists")
    else:
        print("File does not exists")

if __name__ == '__main__':
    main()