# Write a program which accept one number form user and return addition of its factors.

# Input: 12

# Output: 16  (1+2+3+4+6)

def factorSum(iNo):

    iSum = 0

    for x in range(1, int(iNo/2 + 1)):
        
        if (iNo % x == 0):
            iSum = iSum + x
            
    return iSum

def main():

    iValue = int(input("Enter number : "))

    iRet = factorSum(iValue)

    print("Sum of factors is :", iRet)

if __name__ == '__main__':
    main()
