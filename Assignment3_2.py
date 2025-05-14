# Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.

# Input: Number of elements: 7

# Input Elements: 13 5 45 7 4 56 34

# Output: 56

def maximum(data):

    max = data[0]

    for value in data:

        if (max < value):
            max = value

    return max

def main():

    iValue = int(input("Number of elements : "))

    data = []

    print("Input Elements : ")

    for x in range(iValue):
        no = int(input())
        data.append(no)

    iRet = maximum(data)

    print("Output :", iRet)

if __name__ == '__main__':
    main()
