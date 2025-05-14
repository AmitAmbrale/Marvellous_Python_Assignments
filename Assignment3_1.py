# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

# Input: Number of elements: 6
# Input Elements: 13 5 45 7 4 56
# Output: 130

def Sum(data):

    sum = 0

    for x in data:
        sum = sum + x

    return sum

def main():

    iValue = int(input("Number of elements : "))

    data = []

    print("Input Elements : ")
    for x in range(iValue):
        no = int(input())
        data.append(no)

    iRet = Sum(data)

    print("Output :", iRet)

if __name__ == '__main__':
    main()
