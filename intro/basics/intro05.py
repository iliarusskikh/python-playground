class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"{self.name}({self.age})"
  
  def myfunc(self):
    print("Hello my name is " + self.name)
  def printname(self):
    print(self.firstname, self.age)
    

class Student(Person):
    def __init__(self, fname, lname): #this func overrides parent class func
        Person.__init__(self, fname, lname)#however this would keep the parental call
        #super().__init__(fname, lname) #this inherits all from paretnal class
  
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

p1.myfunc()
del p1.age

x = Student("Mike", 22)
x.printname()


class Student1(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year



#iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))



#polymorphism

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()
