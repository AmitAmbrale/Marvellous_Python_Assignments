# Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to 
# ChkPrime() function which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime

# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 + 2 + 5)

from MarvellousNum import chkPrime
from MarvellousNum import Sum

def ListNum(Func, data):

    list = []

    for value in data:

        if (Func(value)):
            list.append(value)

    return list

def reduceX(Func, data):

    sum = 0

    for value in data:
        sum = Func(sum, value)

    return sum

def main():

    iValue = int(input("Number of elements : "))

    data = []

    print("Input Elements : ")

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    PData = ListNum(chkPrime, data)

    RData = reduceX(Sum, PData)

    print("Output :", RData)

if __name__ == '__main__':
    main()
