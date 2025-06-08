# Create a class Calculator with methods for add, subtract, multiply, divide. 
# Ask user input for values and call methods accordingly.

class Calculator:

    def __init__(self, No1, No2):
        self.No1 = No1
        self.No2 = No2

    def add(self):
        return self.No1 + self.No2
    
    def subtract(self):
        return self.No1 - self.No2
    
    def multiply(self):
        return self.No1 * self.No2
    
    def division(self):
        result = 0

        try:
            result = self.No1 / self.No2
        except Exception:
            print(end = "")

        return result
    
def main():

    iValue1 = int(input("Enter first number : "))
    iValue2 = int(input("Enter second number : "))

    iAns = 0

    obj1 = Calculator(iValue1, iValue2)

    Ans = obj1.add()
    print("Addition :", Ans)

    Ans = obj1.subtract()
    print("Subtraction :", Ans)

    Ans = obj1.multiply()
    print("Multiplication :", Ans)

    Ans = obj1.division()
    print("Division :", Ans)

if __name__ == '__main__':
    main()
