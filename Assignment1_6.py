# Write a program which accept number from user and check whether that number is positive or negative or zero.

#   Input: 11
#   Output: Positive Number

#   Input: -8
#   Output: Negative Number

#   Input: 0
#   Output: Zero

def chkPosNeg(iNo):

    if (iNo == 0):
        print("Zero")
    elif (iNo > 0):
        print("Positive")
    else:
        print("Negative")

def main():
    
    print("Enter number :")
    iValue = int(input())

    chkPosNeg(iValue)

if __name__ == "__main__":
    main()