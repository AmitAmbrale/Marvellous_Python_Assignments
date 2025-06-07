# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. Reduce will return addition of 
# all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

# List after filter = [2, 4, 4, 2, 8, 10]

# List after map = [4, 16, 16, 4, 64, 100]

# Output of reduce = 204

Even = lambda No : (No % 2 == 0)

Increase = lambda No : (No**2)

Sum = lambda No1, No2  : (No1 + No2)

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

    sum = 0

    for value in data:

        sum = Func(value, sum)

    return sum

def main():

    iValue = int(input("Enter size : "))

    data = []

    for i in range(iValue):
        no = int(input())
        data.append(no)

    Fdata = filterX(Even, data)

    print(Fdata)

    Mdata = mapX(Increase, Fdata)

    print(Mdata)

    Rdata = reduceX(Sum, Mdata)

    print("Output : ", Rdata)

if __name__ == '__main__':
    main()
