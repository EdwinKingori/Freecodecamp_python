class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) #using the super() function without using the name of the parent element. (It automatically inherits the ethods and properties from its parent.
    self.graduationyear = year # Adding the property graduationyear to the student class

  def welcome(self): # Adding a method called welcome to the sudent class.
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
