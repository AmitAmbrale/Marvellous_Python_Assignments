# Create a class Vehicle with method start(). Derive class Car and override the method start() with additional behavior. Show method overriding.

class Vehicle:

    def start(self):
        print("Inside Vehicle::start()")

class Car(Vehicle):

    def start(self):
        print("Inside Car::start()")

def main():

    vobj = Vehicle()
    vobj.start()

    cobj = Car()
    cobj.start()

if __name__ == '__main__':
    main()
