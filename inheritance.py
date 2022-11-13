#Learning, inheritance from parent to child
#Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
# Child class
class Student(Person):
  def __init__(self, fname, lname):
      #parent.__init__(self,fname,lname) this helps in preventig the child's __init__ function from overriding the parent function.
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print("Name: ", x.firstname, x.lastname,"\nGraduation Year: ",  x.graduationyear)
