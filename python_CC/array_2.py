class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("john", "Doe")
x.printname()

class Student(Person):
    pass

x = Student("Mike","Olsen")
x2 = Student("Jesus","Garmendia")

x.printname()
x2.printname()