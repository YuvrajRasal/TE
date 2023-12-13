class Person:
 def __init__(self, fname, lname, age):
     self.firstname = fname
     self.lastname = lname
     self.age = age
 
 def printName(self):
     print(self.firstname, self.lastname)
p1 = Person(input("Enter first name: "), input("Enter last name: "), input("Enter age: "))
p1.printName()
p1.firstname = "Devraj"
p1.printName()
print("Age is:", p1.age)
del p1.age # deleting object property
del p1 # deleting object