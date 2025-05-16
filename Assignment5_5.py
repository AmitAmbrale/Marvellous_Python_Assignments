# Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.

# Expected Input:
# Enter a number: 17
# Expected Output: 17 is an odd number.

EvenOdd = lambda iNo : (iNo % 2 == 0)

def main():

    iValue = int(input("Enter a number : "))

    bRet = EvenOdd(iValue)

    if(bRet):
        print(iValue,"is an even number.")
    else:
        print(iValue,"is an odd number.")

if __name__ == '__main__':
    main()
