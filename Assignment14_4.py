# Create a class Student with name, roll_no, and a class variable school_name. Print student details and 
# school name. Change the school name using class name.

class Student:

    School_name = "Marvellous Infosystems"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def DisplayDetails(self):
        print("Name of student :", self.name)
        print("Roll no of student :", self.roll_no)
        print("School name :", Student.School_name)

    @classmethod
    def changeSchoolName(cls):
        Student.School_name = "New Era High School"

def main():

    obj = Student("Amit", 159)

    obj.DisplayDetails()

    obj.changeSchoolName()

    obj.DisplayDetails()

if __name__ == '__main__':
    main()
