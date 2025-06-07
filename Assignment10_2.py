# Write a program which contains one lambda function which accepts two parameters and 
# return its multiplication.

# Input: 4 3

# Output: 12

# Input: 6 3

# Output: 18

Multiply = lambda No1, No2 : No1 * No2

def main():

    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))

    result = Multiply(iValue1, iValue2)

    print("Output :", result)

if __name__ == '__main__':
    main()
