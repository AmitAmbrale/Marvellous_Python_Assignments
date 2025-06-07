# Write a program which contains one class named as Demo.
# Demo class contains two instance variables as noi, no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 Demo (11,21) Obj2 Demo(51,101)
# Now call the instance methods as

# Obj1.Fun()

# Obj2.Fun()

# Obj1.Gun()

# Obj2.Gun()

class Demo:

    value = 10

    def __init__(self,No1, No2):
        self.No1 = No1
        self.No2 = No2
    
    def Fun(self):
        print("Inside Fun()")
        print("No1 : ", self.No1)
        print("No2 : ", self.No2)

    def Gun(self):
        print("Inside Gun()")
        print("No1 : ", self.No1)
        print("No2 : ", self.No2)

def main():

    print("Class variable :", Demo.value)

    dobj1 = Demo(11, 21)
    dobj2 = Demo(51, 101)

    dobj1.Fun()
    dobj1.Gun()

    dobj2.Fun()
    dobj2.Gun()

if __name__ == "__main__":
    main()