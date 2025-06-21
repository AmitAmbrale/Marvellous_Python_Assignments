# Write a script to remove all blank lines from a file. 
# Save the cleaned output to a new file.

import os

def RemoveBlankLines(fname):

    if(os.path.exists(fname) == False):
        print("No such file present")
        exit()

    if(os.path.isfile(fname) == False):
        print("Given input is not a file")
        exit()

    if(os.path.isabs(fname) == False):
        fname = os.path.abspath(fname)
    
    fobj = open(fname, 'r')
    nobj = open("CleanedFile.txt", 'w')

    numLines = fobj.readlines()

    for line in numLines:

        if line.strip(): 
            nobj.write(line)

    fobj.close()
    nobj.close()

def main():

    FileName = input("Enter name of file : ")

    RemoveBlankLines(FileName)

if __name__ == '__main__':
    main()
