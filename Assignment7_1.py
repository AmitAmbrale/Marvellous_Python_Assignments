# Write two lambda functions:

# One to calculate square of a number
# Another to calculate cube of a number

# Expected Input:
# Enter a number: 3

# Expected Output:
# Square: 9
# Cube : 27

Square = lambda iNo : (iNo**2)

Cube = lambda iNo : (iNo**3)

def main():

    iValue = int(input("Enter a number : "))

    iRet = 0

    iRet = Square(iValue)
    print("Square :", iRet)

    iRet = Cube(iValue)
    print("Cube :", iRet)

if __name__ == '__main__':
    main()
