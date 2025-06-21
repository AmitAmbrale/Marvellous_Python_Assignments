# Write a program which accept file name from user and open that file 
# and display the contents of that file on screen.
# Input: Demo.txt
# Display contents of Demo.txt on console.

import os

def displayContents(FileName):

    if (os.path.exists(FileName) == False or os.path.isfile(FileName) == False):
        print("No such file present in current directory")
        exit()

    if (os.path.isabs(FileName) == False):
        FileName = os.path.abspath(FileName)

    fobj = open(FileName, mode = "r")

    data = fobj.read()

    print("Data :", data)

    fobj.close()

def main():

    FName = input("Enter file name : ")

    displayContents(FName)

if __name__ == '__main__':
    main()
