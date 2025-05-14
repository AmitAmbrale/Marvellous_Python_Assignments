# Create on module named as Arithmetic which contains 4 functions as Add() for addition, 
# Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by 
# accepting the parameters from user.

import Arithmetic
import sys

def main():

    if (len(sys.argv) == 2):

        if(sys.argv[1] == "--h"):
            print("This application is used to perform arithmetic operations on two numbers")
            return

        if(sys.argv[1] == "--u"):
            print("Execute the code as")
            print("python Filename.py Input1 Input2")
            return

    if(len(sys.argv) != 3):

        print("Insufficient number of arguements")
        print("You can use --h for Help & --u for Usage")
        return
    
    iValue1 = int(sys.argv[1])
    iValue2 = int(sys.argv[2])

    iRet = 0

    iRet = Arithmetic.Add(iValue1, iValue2)

    print("Addition is : ", iRet)

    iRet = Arithmetic.Sub(iValue1, iValue2)

    print("Substraction is : ", iRet)

    iRet = Arithmetic.Mul(iValue1, iValue2)

    print("Multiplication is : ", iRet)

    iRet = Arithmetic.Div(iValue1, iValue2)

    print("Division is : ", iRet)

if __name__ == '__main__':
    main()
