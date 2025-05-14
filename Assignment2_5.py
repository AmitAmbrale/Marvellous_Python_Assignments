# Write a program which accept one number for user and check whether number is prime or not.

# Input: 5

# Output: It is Prime Number

def chkPrime(iNo):

    bFlag = True

    for x in range(2, int(iNo/2 + 1)):
        
        if (iNo % x == 0):
            bFlag = False
            break
        
    return bFlag

def main():

    iValue = int(input("Enter number : "))

    bRet = chkPrime(iValue)

    if(bRet):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == '__main__':
    main()
