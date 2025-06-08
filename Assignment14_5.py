# Create a class BankAccount with account_number, name, and balance. 
# Use init and create methods for deposit, withdraw, and displaying balance

class BankAccount:

    def __init__(self,name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def depoist(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def display(self):
        print("Name :", self.name)
        print("Account Number :", self.account_number)
        print("Balance :", self.balance)
        
def main():

    obj1 = BankAccount("Amit", 1272240621, 2000)

if __name__ == '__main__':
    main()
