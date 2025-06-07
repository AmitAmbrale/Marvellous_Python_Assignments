# Count Zeros in a Number (Recursively)
# Write a recursive function to count how many zeros are in the given number.

# count_zeros (1020300)→4

count = 0

def count_zeros(No):

    global count

    if (No == 0):
        return
    else:
        if(No % 10 == 0):
            count = count + 1
        No = int(No/10)
        count_zeros(No)

def main():

    iValue = int(input("Enter number : "))

    count_zeros(iValue)

    print("Output :", count)
    
if __name__ == '__main__':
    main()
