
class Dog(object):
    dogs = []
    def __init__(self, name):
        self.name = name
        print("Dog init")
        self.dogs.append(self)
        
    def speak(self):
        print("This is", self.name)
    
    @classmethod
    def num_dogs(cls)
        return len(cls.dogs)
    
    @staticmethod
    def bark(n)
        """barks n times"""
        for _ in range(n):
            print("Bark!")


tim = Dog('Tim')


class Cat(Dog):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
        

print(Dog.dogs)
Dog.bark(4)


class _Private:
    def __init__(self,name):
        self.name = name

class NotPrivate:
    def __init__(self,name)
        self.name = name
        self.priv = _Private(name)
        
    def _display(self):
        print("Hello")
        
        
    def display(self):
        print("Hi")
