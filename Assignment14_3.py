# Create a class Book with private attribute _ price. Add methods to get and set the price. Show encapsulation.

class Book:

    def __init__(self):
        self.__price = 0
    
    def SetPrice(self, No):
        self.__price = No

    def GetPrice(self):
        return self.__price
    
def main():

    obj1 = Book()

    obj1.SetPrice(4355)

    print("Price :", obj1.GetPrice())

    obj1 = Book()

    obj1.SetPrice(3255)

    print("Price :", obj1.GetPrice())

if __name__ == '__main__':
    main()
