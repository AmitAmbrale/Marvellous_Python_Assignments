# Arithmetic Operations on Two Numbers
# Write a program to accept two integers from the user and display their:

# Sum
# Difference
# Product
# Division

# Expected Input:
# Enter first number: 10
# Enter second number: 2

# Expected Output:
# Sum : 12
# Difference : 8
# Product : 20
# Division : 5.0

from sys import argv

Sum = lambda iNo1, iNo2 : (iNo1 + iNo2)
Difference = lambda iNo1, iNo2 : (iNo1 - iNo2)
Product = lambda iNo1, iNo2 : (iNo1 * iNo2)

def Division(iNo1, iNo2):

    iAns = 0

    if (iNo2 == 0):
        return "undefined"
    
    iAns = iNo1/iNo2

    return iAns

def main():

    if (len(argv) == 2):

        if(argv[1] == "--h"):
            print("This application is used to perform arithmetic operations on two numbers")
            return

        if(argv[1] == "--u"):
            print("Execute the code as")
            print("python Filename.py Input1 Input2")
            return

    if(len(argv) != 3):

        print("Insufficient number of arguements provided")
        print("You can use --h for Help & --u for Usage")
        return

    iValue1 = int(argv[1])
    iValue2 = int(argv[2])

    iRet = 0

    iRet = Sum(iValue1, iValue2)

    print("Sum :", iRet)

    iRet = Difference(iValue1, iValue2)

    print("Difference :", iRet)

    iRet = Product(iValue1, iValue2)

    print("Product :", iRet)

    iRet = Division(iValue1, iValue2)

    print("Division :", iRet)

if __name__ == '__main__':
    main()
