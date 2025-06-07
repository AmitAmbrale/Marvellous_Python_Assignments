# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount. That class contains one class variable as ROI which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest().
# Deposit() method will accept the amount from user and add that value in class instance variable Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
# which is Class variable as ROI.
# And Display() method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:

    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print("Name :", self.Name)
        print("Amount :", self.Amount)

    def Deposit(self, amt): 
        self.Amount = self.Amount + amt

    def Withdraw(self, amt): 
        self.Amount = self.Amount - amt

    def CalculateIntrest(self):
        intrest = (self.Amount * BankAccount.ROI)/100
        return intrest

def main():

    bobj1 = BankAccount("Amit", 5000)

    bobj1.Deposit(1000)

    bobj1.Withdraw(230)

    bobj1.Display()
    print("Interest :", bobj1.CalculateIntrest())

    bobj2 = BankAccount("AmitAmbrale", 2000)

    bobj2.Deposit(300)

    bobj2.Withdraw(940)

    bobj2.Display()
    print("Interest :", bobj2.CalculateIntrest())

if __name__ == "__main__":
    main()