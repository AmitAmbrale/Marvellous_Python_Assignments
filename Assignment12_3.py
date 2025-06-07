# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Valuel, Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1, Value2 and return result.
# Subtraction() method will perform subtraction of Value1, Value2 and return result. Multiplication() method will perform multiplication of Value1, Value2 and return result.
# Division() method will perform division of Value1, Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        iValue1 = int(input("Enter first number : "))
        iValue2 = int(input("Enter second number : "))

        self.value1 = iValue1
        self.value2 = iValue2

    def Addition(self):
        result = 0

        result = self.value1 + self.value2

        return result
    
    def Subtraction(self):
        result = 0

        result = self.value1 - self.value2

        return result
    
    def Multiplication(self):
        result = 0

        result = self.value1 * self.value2

        return result
    
    def Division(self):
        result = 0

        try:
            result = self.value1 / self.value2
        except Exception:
            print(end = "")
            
        return result

def main():

    aobj = Arithmetic()

    aobj.Accept()

    ans = aobj.Addition()

    print("Addition is :", ans)

    ans = aobj.Subtraction()

    print("Subtraction is :", ans)

    ans = aobj.Multiplication()

    print("Multiplication is :", ans)

    ans = aobj.Division()

    print("Division is :", ans)

if __name__ == '__main__':
    main()
