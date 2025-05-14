# Write a program which accept number from user and return number of digits in that number

# Input :  5187934
# Output : 7

def countDigits(iNo):

    count = 0

    if (iNo < 0):
        iNo = -iNo

    while(iNo != 0):
        count += 1
        iNo = int(iNo / 10)
    
    return count

def main():

    iValue = int(input("Enter number : "))

    iRet = countDigits(iValue)

    print("Number of digits :", iRet)

if __name__ == "__main__":
    main()
