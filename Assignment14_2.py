# Write a class Rectangle with length and width. Add a method to compute area and perimeter.

# Area: 50, Perimeter: 30

class Rectangle:

    def __init__(self, l, w):
        self.length = l
        self.width = w
    
    def calArea(self):
        result = 0
        result = self.length * self.width
        return result
    
    def calPerimeter(self):
        result = 0
        result = 2 * (self.length + self.width)
        return result
    
def main():

    obj1 = Rectangle(4,5)

    print("Area is :", obj1.calArea())

    print("Perimeter :", obj1.calPerimeter())

if __name__ == '__main__':
    main()
