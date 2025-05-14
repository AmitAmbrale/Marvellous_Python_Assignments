# Write a program which accept number from user and return addition of digits in that number.

# Input :  5187934
# Output : 37

def digitSum(iNo):

    sum = 0

    if (iNo < 0):
        iNo = -iNo

    while(iNo != 0):
        sum += (iNo % 10)
        iNo = int(iNo / 10)
    
    return sum

def main():

    iValue = int(input("Enter number : "))

    iRet = digitSum(iValue)

    print("Sum of digits :", iRet)

if __name__ == "__main__":
    main()
