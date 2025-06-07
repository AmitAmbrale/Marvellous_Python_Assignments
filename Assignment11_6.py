# Sum of First N Natural Numbers
# Write a recursive function to calculate sum from 1 to n.

# sum_n(5)→15

sum = 0

def sum_n(No):

    global sum

    if (No == 0):
        return
    else:
        sum = sum + No
        No = No - 1
        sum_n(No)

def main():

    iValue = int(input("Enter number : "))

    sum_n(iValue)

    print("Output :", sum)

if __name__ == '__main__':
    main()
