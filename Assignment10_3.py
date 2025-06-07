# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 
# and less than or equal to 90. Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

# Input List [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

# List after filter = [76, 89, 86, 90, 70]

# List after map [86, 99, 96, 100, 80]

# Output of reduce = 6538752000

Compare = lambda No : ((No >= 70) and (No <= 90))

Increase = lambda No : (No + 10)

Product = lambda No1, No2  : (No1 * No2)

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

    product = 1

    for value in data:

        product = Func(value, product)

    return product

def main():

    iValue = int(input("Enter size : "))

    data = []

    for i in range(iValue):
        no = int(input())
        data.append(no)

    Fdata = filterX(Compare, data)

    Mdata = mapX(Increase, Fdata)

    Rdata = reduceX(Product, Mdata)

    print("Output : ", Rdata)

if __name__ == '__main__':
    main()

