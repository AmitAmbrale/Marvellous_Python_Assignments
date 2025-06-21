# Write a Python script to count the number of lines, words, and 
# characters in a given file.

import os
import sys

def CountLines(fname):

    fobj = open(fname, 'r')

    ret = fobj.readlines()

    return len(ret)

def DisplayDetails(fname):

    if (os.path.exists(fname) == False):
        print("No such file present")
        exit()
    if (os.path.isfile(fname) == False):
        print("Given input is not a file")
        exit()
    
    if(os.path.isabs(fname) == False):
        fname = os.path.abspath(fname)

    fobj = open(fname, 'r')

    countLines = CountLines(fname)
    countWords = 0
    countChar = 0

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        List = buffer.split()
        countWords = countWords + len(List)
        countChar = countChar + len(buffer)
        buffer = fobj.read(1024)

    return countLines, countWords, countChar

def main():

    if (len(sys.argv) == 2):

        if (sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to count number of Lines, Words and Chracters from a file")
        elif (sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("You can use this appliation as :")
            print("Usage : ScriptName.py  FileName.txt")
        else:
            fname = sys.argv[1]

            line, word, charX = DisplayDetails(fname)

            print("Number of Lines :", line)
            print("Number of Words :", word)
            print("Number of Characters :", charX)
    else:
        print("Invalid number of arguements")
        print("Use --h to know the application")
        print("Use --u to understand how to run the application")
if __name__ == '__main__':
    main()