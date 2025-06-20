import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result
        
    return wrapper
    
@timer
def example_func(n)
    return f"the sum is {sum(range(n)}"
    
print(example_func(10000))


"""___________________________________________________________"""
class Circle:
    def __init__(self, radius):
        self._rad = radius
        
    @property
    def radius(self,value):
        return self._rad
        
    @radius.setter #to access c.radius
    def radius(self,value):
        if value >= 0:
            self._rad = value
        else:
            raise ValueError("Radius must be positive")
            
    @property
    def diameter(self)
        return self._rad * 2
        
    @radius.deleter
    def radius(self):
        del self._rad
        
        
c = Circle(4)
print(c.radius)
print(c.diameter)
c.radius = 5 #setter

del c.radius

"""___________________________________________________________"""
#no need to create an instance of Math class, just use the methods
class Math:
    @staticmethod
    def add(x,y):
        return y+x
        
print(Math.add(5,6))


"""___________________________________________________________"""

class Person:
    species = "Human beings"
    
    @classmethod
    def get_species(cls):
        return cls.species#accessing only class attributes, methods
        
print(Person.get_species())#transform the first implicit parameter to be an instance of a class, not an individual object


"""___________________________________________________________"""
import functools

def fibonacci(n):
    if n <2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    
#1,1,2,3,5,8
print(fibonacci(10))
#we need to cash the recursive results to reuse

def fib(n, cache={}):
    if n in cache:
        return cache[n]
        
    if n == 0:
        return 0
    elif n == 1:
        return 1
        
    cache[n] = fib(n-1, cache) + fib(n-2, cache)
    return cache[n]
    #kinda dynamic programming

@functools.cache
def fibo(n):
    if n <2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)



"""___________________________________________________________"""



from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: str
    quantity: int = 0
    
    def total_cost(self) -> float:
        return self.price * self.quantity
        
p1 = Product(name="Laptop", price=100.0, quantity = 3)
print(p1.total_cost())

