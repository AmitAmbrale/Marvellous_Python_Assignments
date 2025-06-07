# Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius, Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14.
# Inside init method initialise all instance variables to 0.0.
# There are three instance methods inside class as Accept(), CalculateArea(),
# CalculateCircumference(), Display().
# Accept method will accept value of Radius from user.
# CalculateArea() method will calculate area of circle and store it into instance variable Area.
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable Circumference.
# And Display() method will display value of all the instance variables as Radius Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects.

class Circle:

    PI = 3.14

    def __init__(self):
        self.No1 = 0.0
        self.No2 = 0.0
        self.No3 = 0.0

    def Accept(self, rad):
        self.No1 = rad
    
    def CalculateArea(self):
        self.No2 = self.No1 * self.No1 * Circle.PI

    def CalculateCircumference(self):
        self.No3 = 2 * Circle.PI * self.No1

    def Display(self):
        print("Given Radius :", self.No1)
        print("Area of circle :", self.No2)
        print("Circumference of circle :", self.No3)

def main():

    iValue = int(input("Enter radius : "))

    cobj = Circle()

    cobj.Accept(iValue)

    cobj.CalculateArea()

    cobj.CalculateCircumference()

    cobj.Display()

if __name__ == "__main__":
    main()
