# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

EvenNo = lambda iNo : (iNo % 2 == 0)

def filterX(Func, data):

    list = []

    for value in data:
        if (Func(value)):
            list.append(value)

    return list

Square = lambda iNo : (iNo**2)

def mapX(Func, data):

    list = []

    for value in data:
        list.append(Func(value))

    return list

Add = lambda iNo1, iNo2 : (iNo1 + iNo2)

def reduceX(Func, data):

    sum = 0

    for value in data:
        sum = Func(value, sum)

    return sum

def main():

    iSize = int(input("Enter size : "))

    data = []

    for x in range(iSize):
        no = int(input())
        data.append(no)

    print("Input List :",data)

    FData = filterX(EvenNo, data)

    print("List after filter :",FData)

    MData = mapX(Square, FData)

    print("List after map :", MData)

    RData = reduceX(Add, MData)

    print("Output of reduce :", RData)

if __name__ == '__main__':
    main()
