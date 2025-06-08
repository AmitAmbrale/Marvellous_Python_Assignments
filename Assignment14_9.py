# Create a class Product with attributes name and price. Implement eq method to 
# compare two products if they are equal in price.

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self,Obj):

        if((self.name == Obj.name) and (self.price == Obj.price)):
            return True
        else:
            return False
def main():

    pobj1 = Product("Amit", 30000)
    pobj2 = Product("Amit", 30000)
    pobj3 = Product("Akshay", 40000)

    print(pobj1 == pobj2)
    print(pobj2 == pobj3)

if __name__ == '__main__':
    main()
