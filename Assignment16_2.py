# Write a program to read and display the contents of a file data.txt.

import os

def DisplayContents(fname):

    if (os.path.exists(fname) == False):
        print("No such file present")
        exit()
    if (os.path.isfile(fname) == False):
        print("Given input is not a file")
        exit()
    
    if(os.path.isabs(fname) == False):
        fname = os.path.abspath(fname)

    fobj = open(fname, 'r')

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        print(buffer)
        buffer = fobj.read(1024)
    
    fobj.close()

def main():

    fname = input("Enter file name : ")

    DisplayContents(fname)

if __name__ == '__main__':
    main()
