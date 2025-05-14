# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5

# Output: 3

def countElement(data, search):

    count = 0

    for value in data:

        if (value == search):
            count += 1
    
    return count

def main():

    iValue = int(input("Number of elements : "))

    data = []

    print("Input Elements : ")

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    search = int(input("Element to search : "))

    iRet = countElement(data, search)

    print("Output :", iRet)

if __name__ == '__main__':
    main()
