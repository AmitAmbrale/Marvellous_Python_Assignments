# Write a function that accepts a list of integers and returns a list of prime numbers using filter().

# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17

# Expected Output:
# Prime numbers: [11, 13, 17]

def chkPrime(iNo):

    bFlag = True

    for x in range(2, int(iNo/2 + 1)):

        if (iNo % 2 == 0):
            bFlag = False
            break
    
    return bFlag

def filterX(Func, data):

    list = []

    for value in data:
        if(Func(value)):
            list.append(value)

    return list

def main():

    iValue = int(input("Enter size : "))

    data = []

    for x in range(iValue):
        no = int(input())
        data.append(no)
    
    FData = filterX(chkPrime, data)

    print("Prime numbers :", FData)

if __name__ == '__main__':
    main()