# Create a base class Person with name and age. Derive a class Teacher with subject and salary. 
# Use super() to call base class constructor and print both.

class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def Display(self):
        print("Name :", self.name)
        print("Age :", self.age)

class Teacher(Person):

    def __init__(self, subject, salary):
        super().__init__("Amit", 21)
        self.subject = subject
        self.salary = salary

    def Display(self):
        # print("Name :", self.name)
        # print("Age :", self.age)
        super().Display()
        print("Subject :", self.subject)
        print("Salary :", self.salary)

def main():

    tobj = Teacher("Maths", 25000)

    tobj.Display()

if __name__ == '__main__':
    main()
