# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 

# Input List = [2, 70, 11, 10, 17, 23, 31, 77]

# List after filter = [2, 11, 17, 23, 31] 

# List after map = [4, 22, 34, 46, 62]

# Output of reduce = 62

def Prime(No):
    bFlag = True

    for i in range(2, int(No/2 + 1)):
        if(No % i == 0):
            bFlag = False
            break

    return bFlag

def Increase(No):
    return No*2

def Maximum(No1, No2):

    if(No1 > No2):
        return No1
    else:
        return No2    

def filterX(Func, data):

    list = []

    for value in data:

        if (Func(value)):
            list.append(value)

    return list

def mapX(Func, data):

    list = []

    for value in data:

        list.append(Func(value))

    return list

def reduceX(Func, data):

    max = data[0]

    for value in data:

        max = Func(max, value)
    
    return max

def main():

    iValue = int(input("Enter size : "))

    data = []

    for i in range(iValue):
        no = int(input())
        data.append(no)

    Fdata = filterX(Prime, data)

    print(Fdata)

    Mdata = mapX(Increase, Fdata)

    print(Mdata)

    Rdata = reduceX(Maximum, Mdata)

    print("Output : ", Rdata)

if __name__ == '__main__':
    main()
