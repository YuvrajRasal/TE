class Person:
 def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
 
 def printName(self):
    print(self.firstname, self.lastname)
    
class Student(Person):
 def __init__(self, fname, lname): 
 # Person.__init__(self, fname, lname)
    super().__init__(fname, lname) # Here self isn't required
    
x = Student(input("Enter first name: "), input("Enter last name: "))
x.printName()
