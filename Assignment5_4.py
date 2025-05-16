# Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.

# Expected Input:
# Enter three numbers: 5    9   3
# Expected Output: Largest number is 9.

def Largest(iNo1, iNo2, iNo3):

    if(iNo1 > iNo2 and iNo1 > iNo3):
        return iNo1
    elif (iNo2 > iNo1 and iNo2 > iNo3):
        return iNo2
    else:
        return iNo3

def main():

    iValue1 = int(input("Enter three numbers : "))
    iValue2 = int(input())
    iValue3 = int(input())
 
    iRet = Largest(iValue1, iValue2, iValue3)

    print("Largest number is :", iRet)

if __name__ == '__main__':
    main()

