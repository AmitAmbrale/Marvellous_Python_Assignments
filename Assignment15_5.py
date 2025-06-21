# Accept file name and one string from user and return the frequency of that string from file.

# Input: Demo.txt Marvellous

# Search "Marvellous" in Demo.txt

import os
import sys

def CalculateFrequency(fname, data):

    if (os.path.exists(fname) == False):
        print("No such file present in current directory")
        exit()
    
    if(os.path.isfile(fname) == False):
        print("Given input is not a file")
        exit()

    if (os.path.isabs(fname) == False):
        fname = os.path.abspath(fname)

    fobj = open(fname, 'r')
    count = 0

    buffer = fobj.read(1024)

    while(len(buffer) > 0):
        count = count + buffer.count(data)
        buffer = fobj.read(1024)
    
    return count

def main():

    if(len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to calculate the frequency of a string from a file")    
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  FileName.txt String") 
            print("Plz provide valid absolute path")  
        else:
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")
    elif (len(sys.argv) == 3):
        Fname1 = sys.argv[1]
        data = sys.argv[2]
        ret = CalculateFrequency(Fname1, data)
        print("Frequency :", ret)
    else:
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == '__main__':
    main()