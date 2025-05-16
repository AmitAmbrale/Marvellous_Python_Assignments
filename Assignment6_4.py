# Accept a number and print its factorial using a for loop.

# Expected Input:
# Enter a number: 5

# Expected Output:
# Factorial of 5 is: 120

def factorial(iNo):

    ifact = 1

    for x in range(1,iNo+1):

        ifact = ifact * x

    return ifact

def main():

    iValue = int(input("Enter a number : "))

    iRet = 0

    iRet = factorial(iValue)

    print("Factorial of ", iValue, "is :", iRet)

if __name__ == '__main__':
    main()
