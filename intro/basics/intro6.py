import inspect

def func1():
    print("Hello")
    
fun = func1()
print(id(fun))#returns mem address
print(inspect.getsource(fun))


x = [1,2,3]
y = [4,5]

print(x+y)
print(x[1])
print(len(x))


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"
    
    def __call__(self,y):
        print("called this function", y)
    
p = Person("Will")
print(p)
p(4)




#metaclasses and how to use it!
class Test:
    pass

print(Test)
print(Test()) #is an object
print(type(Test))# class 'type' metaclass

def add_attribute(self):
    self.z = 9

Test1 = type('Test1', (), {"x":5, "add_attribute":add_attribute})#equivalent to defining a class
t = Test1
print(t.x)
t.we = "Hello"



class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        a = {}
        for name, value in attrs.items():
            if name.startswith("__"):
                a[name] = value
            else:
                a[name.upper()] = value
        
        return type(class_name, bases, attrs)
    
    #def __init__():

class Dog(metaclass=Meta):
    x = 5
    y = 8
    
    def hello(self):
        print("Hello")
    





#decorators
def func(f):
    def wrapper(*args,**kwargs):#any numner positional arguments
        print("Started")
        rv = f(*args,**kwargs)
        print("ended")
        return rv
        
    return wrapper

def func2():
    print("Func 2")
        
x = func(func2)
x()

#or
func2 = func(func2)
func2()

#or
@func
def func3(x):
    print(f"Func 3{x}")
    
func3(5)

@func
def func5(x,y):
    print(f"Func 3{x}")

func5(2,5)




import time

def timer(func):
    def wrapper(*args,**kwargs)
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Time: ", total)
        return rv
        
    return wrapper
  
@timer
def test():
    for _ in range(1000):
        pass

test()

@timer
def test2():
    time.sleep(2)
    
test2()



""" _________________________________________________________________"""



#generators allow looking at one value at a time instead of generating entire list

#x = [i**2 for i in range(10000000000)]
#for el in x:
 #   print(el)
 
class Gen():
    def __init__(self,n):
        self.n = n
        self.last = 0
        
    def __next__(self):
        return self.next()
        
    def next(self):
        if self.last == self.n:
            raise StopIteration()
            
        rv = self.last ** 2
        self.last +=1
        return rv

g = Gen(100)

while True:
    try:
        print(next(g))
    except StopIteration:
        break
        
    
#alternatively

def gen(n):
    for i in range(n):
        yield i**2 #executes once then pauses until this function is caled again
        
g = gen(100)
for i in g:
    print(i)#every time i in g called, execution continues, then returns next yield

#or
print(next(g))
print(next(g))
print(next(g))#next can be used as well

import sys

print(sys.getsizeof(g))#bytes used






""" _________________________________________________________________"""


#context managers


with open("file.txt","r") as file:
    file.write("hello")


class File:
    def __init__(self,filename,method):
        self.file = open(filename, method)
    
    def __enter__(self):
        print("Enter")
        return self.file
    
    def __exit__(self,type,value,traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        #if type == Exception:
        #    return True #to handle exception

with File("file.txt", "w") as f:
    print("Middle")
    f.write("Hello!")
    raise Exception() #still closes the file
    



import contextlib
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    file = open(filename,method)
    print("enter")
    yield file
    file.close()
    print("exit")
    
with file("text.txt", "w") as f:
    print("middle")
    f.write("hello")
