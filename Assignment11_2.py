# Factorial Using Recursion
# Write a recursive function to calculate factorial of a number.

# factorial(5)→120

fact = 1

def Factorial(No):

    global fact

    if (No <= 0):
        return
    else:
        fact = fact * No
        No = No - 1
        Factorial(No)

def main():

    iValue = int(input("Enter number : "))

    Factorial(iValue)

    print("Output :", fact)

if __name__ == '__main__':
    main()
