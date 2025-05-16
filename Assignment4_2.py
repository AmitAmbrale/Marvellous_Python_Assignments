# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

# Input: 4  3

# Output: 12

# Input: 6  3

# Output: 18

Multiply = lambda iNo1, iNo2 : (iNo1 * iNo2)

def main():

    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))

    iRet = Multiply(iValue1, iValue2)

    print("Output :", iRet)

if __name__ == '__main__':
    main()