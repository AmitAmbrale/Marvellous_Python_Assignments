# Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and 
# print the sum of all even numbers from 1 to 100.
# Expected Output: Sum of even numbers between 1 to 100 is: 2550

def evenSum():
    sum = 0

    for x in range(2,101,2):
        sum = sum + x

    return sum

def main():

    iRet = 0

    iRet = evenSum()

    print("Sum of even numbers between 1 to 100 is :", iRet)

if __name__ == '__main__':
    main()
