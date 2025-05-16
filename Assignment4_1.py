# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.

# Input: 4    Output: 16
# Input: 6    Output: 64

Power = lambda iNo: (iNo**2)

def main():

    iValue = int(input("Enter number : "))

    iRet = Power(iValue)

    print("Output :", iRet)

if __name__ == '__main__':
    main()
