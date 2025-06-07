# Sum of Digits
# Write a recursive function to calculate the sum of digits of a number.

# sum_of_digits (1234)→10

sum = 0

def sum_of_digits(No):

    global sum

    if (No <= 0):
        return 
    else:
        sum = sum + (No%10)
        No = int(No / 10)
        sum_of_digits(No)

def main():

    iValue = int(input("Enter number : "))

    sum_of_digits(iValue)

    print("Output :", sum)

if __name__ == '__main__':
    main()
