# Accept a number from the user and check whether it is prime or not.

# Expected Input:
# Enter a number: 11

# Expected Output:
# 11 is a prime number.

def chkPrime(iNo):

    bFlag = True

    for x in range(2, int(iNo/2+1)):

        if (iNo % 2 == 0):
            bFlag = False
            break

    return bFlag

def main():

    iValue = int(input("Enter a input : "))

    bRet = chkPrime(iValue)

    if (bRet):
        print(iValue ,"is a prime number.")
    else:
        print(iValue ,"is not a prime number.")

if __name__ == '__main__':
    main()
