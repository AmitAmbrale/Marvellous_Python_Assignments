# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).

# Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] I
# Output of reduce = 62

def chkPrime(iNo):

    bFlag = True

    for x in range(2, int(iNo/2 + 1)):
        if (iNo % x == 0):
            bFlag = False
            break
    
    return bFlag

def filterX(Func, data):

    list = []

    for value in data:

        if (Func(value)):
            list.append(value)

    return list

Multiply = lambda iNo : (iNo*2)

def mapX(Func, data):

    list = []

    for value in data:
        list.append(Func(value))

    return list

def Maximum(iNo1, iNo2):

    if (iNo1 > iNo2):
        return iNo1
    else:
        return iNo2

def reduceX(Func, data):

    max = data[0]

    for value in data:
        max = Func(value, max)

    return max

def main():

    iSize = int(input("Enter size : "))

    data = []

    for x in range(iSize):
        no = int(input())
        data.append(no)

    print("Input List :",data)

    FData = filterX(chkPrime, data)

    print("List after filter :",FData)

    MData = mapX(Multiply, FData)

    print("List after map :", MData)

    RData = reduceX(Maximum, MData)

    print("Output of reduce :", RData)

if __name__ == '__main__':
    main()
