# Demonstrate private, protected and public access modifiers using a class Employee with attributes: _ salary, department, name.

class Demo:

    def __init__(self):
        self.name = "Amit"              # public
        self._rid = 159                 # protected
        self.__password = "Amit@1234"   # private

    def Display(self):
        print("Name :", self.name)
        print("RID :", self._rid)
        print("Password :", self.__password)

def main():

    dobj = Demo()

    print("Name :", dobj.name)
    print("RID :", dobj._rid)
    # print("Password :", dobj.__password)

    dobj.Display()

if __name__ == '__main__':
    main()

