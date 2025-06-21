# Write a program to read a file line by line and display only those lines 
# that contain more than 5 words.

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

    buffer = fobj.readline()

    while(len(buffer) > 0):
        List = buffer.split()

        if (len(List) > 5):
            print(buffer.strip())
        buffer = fobj.readline()
        
    fobj.close()

def main():

    fname = input("Enter file name : ")

    DisplayContents(fname)

if __name__ == '__main__':
    main()
