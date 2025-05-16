# Write a program which contains filter(), map() and reduce() in it. 
#  Python application which contains one list of numbers. 
#  List contains the numbers which are accepted from user. 
#  Filter should filter out all such numbers which greater than or 
#   equal to 70 and less than or equal to 90. 
#  Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80]

# Output of reduce = 6538752000

Range = lambda iNo : ((iNo >= 70) and (iNo <= 90))

def filterX(Func, data):

    list = []

    for value in data:
         if (Func(value)):
              list.append(value)

    return list

Increase = lambda iNo : iNo + 10

def mapX(Func, data):

    list = []

    for value in data:

        list.append(Func(value))

    return list

Product = lambda iNo1, iNo2 : (iNo1 * iNo2)

def reduceX(Func, data):

    product = 1

    for value in data:
        product = Func(product, value)

    return product

def main():

    iSize = int(input("Enter size : "))

    data = []

    for x in range(iSize):
        no = int(input())
        data.append(no)

    print("Input List :",data)

    FData = filterX(Range, data)

    print("List after filter :",FData)

    MData = mapX(Increase, FData)

    print("List after map :", MData)

    RData = reduceX(Product, MData)

    print("Output of reduce :", RData)

if __name__ == '__main__':
    main()
