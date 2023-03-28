class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("john", "Doe")
x.printname()

class Student(Person):
    def __init__(self,fname,lname,year):
        Person.__init__(self,fname,lname)
        self.graduationyear = year
    
    def printstudent(self):
        print(self.firstname, self.lastname, self.graduationyear)
    
    def saludo(self):
        print("Bienvenido,", self.firstname, self.lastname,"te graduaste en el anho", self.graduationyear)

x = Student("Mike","Olsen", 2019)
x2 = Student("Jesus","Garmendia", 2016)


x.printname()
x.printstudent()
x2.printname()
x2.printstudent()

x2.saludo()