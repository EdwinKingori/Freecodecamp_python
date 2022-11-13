
class Animal:
  def walk (self):
    print("Walking...")

class Dog (Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def bark (self):
    print("Woof!")

roger = Dog("TOM", 10)
print(roger.name, roger.age)
roger.bark()