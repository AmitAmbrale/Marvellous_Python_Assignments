# Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.

# Input: Number of elements: 4
# Input Elements: 13 45 7 5
# Output: 5

def minimum(data):

    min = data[0]

    for value in data:

        if (min > value):
            min = value

    return min

def main():

    iValue = int(input("Number of elements : "))

    data = []

    print("Input Elements : ")

    for x in range(iValue):
        no = int(input())
        data.append(no)

    iRet = minimum(data)

    print("Output :", iRet)

if __name__ == '__main__':
    main()
