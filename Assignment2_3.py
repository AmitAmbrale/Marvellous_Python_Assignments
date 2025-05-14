# Write a program which accept one number from user and return its factorial.

# Input: 5

# Output: 120

def calculateFactorial(iNo):

    iFact = 1

    if (iNo < 0):
        iNo = -iNo

    if (iNo == 0):
        return 0
    
    for x in range(1, iNo + 1):

        iFact = iFact * x
    
    return iFact

def main():

    iValue = int(input("Enter number : "))

    iRet = calculateFactorial(iValue)

    print("Factorial of", iValue, "is :", iRet)

if __name__ == '__main__':
    main()
