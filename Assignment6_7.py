# Accept 5 numbers from the user.
# Find the largest number

def Largest(data):

    max = data[0]

    for value in data:
        if max < value:
            max = value

    return max

def main():

    data = []

    print("Enter 5 numbers : ")

    for x in range(5):
        no = int(input())
        data.append(no)
    
    iRet = Largest(data)

    print("Maximum number :", iRet)

if __name__ == '__main__':
    main()