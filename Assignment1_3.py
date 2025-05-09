# Write a program which contains one function named as Add() 
# which accepts two numbers from user and return addition of that two numbers.

def iAddition(iNo1, iNo2):
    
    iResult = 0

    iResult = iNo1 + iNo2

    return iResult

def main():
    
    print("Enter two numbers : ")
    iValue1 = int(input())
    iValue2 = int(input())

    iAns = iAddition(iValue1, iValue2)

    print("Additon is :", iAns)

if __name__ == "__main__":
    main()