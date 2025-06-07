# Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false.
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects

class Arithmetic:

    def __init__(self, No):
        self.Value = No
    
    def ChkPrime(self):

        bFlag = True

        for i in range(2, int(self.Value/2)+1):
            if (self.Value % i == 0):
                bFlag = False

        return bFlag
    
    def ChkPerfect(self):
        
        sum = 0

        for i in range(1, int(self.Value/2) + 1):
            if self.Value % 2 == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):

        print("Factors :", end= " ")

        for i in range(self.Value + 1):
            if self.Value % 2 == 0:
                print(i, end = " ")

    def factorSum(self):

        sum = 0

        for i in range(1, self.Value+1):
            if self.Value % i == 0:
                sum = sum + i

        return sum

def main():

    iValue = int(input("Enter number : "))

    aobj1 = Arithmetic(iValue)

    if (aobj1.ChkPrime()):
        print("Number is prime")
    else:
        print("Number is not prime")

    if (aobj1.ChkPerfect()):
        print("Number is prefect")
    else:
        print("Number is not perfect")

    print("Sum of factors :", aobj1.factorSum())

    iValue2 = int(input("Enter number : "))

    aobj2 = Arithmetic(iValue2)

    if (aobj2.ChkPrime()):
        print("Number is prime")
    else:
        print("Number is not prime")

    if (aobj2.ChkPerfect()):
        print("Number is prefect")
    else:
        print("Number is not perfect")

    print("Sum of factors :", aobj2.factorSum())

if __name__ == '__main__':
    main()
