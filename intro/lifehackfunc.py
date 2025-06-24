import pprint
import json

with open("load.json", "r")as f:
    data = json.load(f)
    
pprint.pprint(data)#nice formatted output



""" ___________________________________"""

from collections import defaultdict

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = defaultdict(int) #creates default value to non existing elements

for word in words:
    word_count[word] += 1# we do not need to check if word exists in a dictionary
    
print(dict(word_count))

""" ___________________________________"""

import pickle #saves py onject in a file, allowing to upload it

class Dog:
    def __init__(self,name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print(f"bark bark")
        
data = Dog("Max", "Yorkshire Terr", 10)

with open("data.pkl","wb") as f:
    pickle.dump(data,f) #saves this object
    
with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
    
print(loaded_data)
loaded_data.bark



""" ___________________________________"""
#any function

numbers = [0,1,2,3]
print(any(numbers))

numbers2 = [-1,-2,0,4]
print(any(num >0 for num in numbers2)) #false

strings = ["apple", "", "banana"]
print(any(s=="" for s in strings))#True

import os
file_paths = ["file1.txt", "file2.txt", "file3.txt"]
print(any(os.path.exists(path) for path in file_paths))
#if any of those files exist in given paths

print(all(os.path.exists(path) for path in file_paths))#if all values are true

""" ___________________________________"""
#enumerate
names = ['Alice','Bob', 'Charlie']

for index, name in enumerate(names, start=1):
    print(f"{index}. {name")


""" ___________________________________"""

from collections import Counter
words = ["apple","banana","apple","orange","banana"]
count = Counter(words)
print(count)
print(count["apple"])


""" ___________________________________"""

import timeit

#list comprehension
code = """
a = [1,2,3,4,5]
b = [x *2 for x in a]
"""

def code2():
    a = [1,2,3,4,5]
    b = list(map(lambda x: x * 2, a))
    
time1 = timeit.timeit(code1, number = 100000)#1m times by default
time2 = timeit.timeit(code2, number = 100000)


""" ___________________________________"""
from itertools import chain

#list addition
list1 = [1,2,3]
list2 = ["a", "b", "c"]
combined_add = list1 + list2 #immediate and mem-intensive

combined_chain = list(chain(list1,list2))#lazy and efficient - creates iteratable object

print(next(combined_chain))


""" ___________________________________"""
 
 def func_called(func, *args, **kwargs)
    return func(*args,**kwargs)
    
def add(a,b):
    return a+b
    
def pow(base=1, exp=1):
    return base ** exp

result = func_called(add,10,11)
print(result)

funcs = [add, pow, add, add]
args = [
        [(1,2),{}],
        [(),{"base": 5, "exp":2}],
        [(5,6), {}],
        [(3,4), {}]
    ]

for func, (args,kwargs) in zip(funcs, args):
    result = func(*args, **kwargs)
    print(result)


""" ___________________________________"""
def adder(value):
    def inner_func(base):
        return base + value
        
    return inner_func
    
adder_5 = adder(5)
result = adder_5(10)#10 + 5


""" ___________________________________"""
x = 10

    nonlocal x
    x = 20

#way to modify outer scop variable from the inner local scope


""" ___________________________________"""
from typing import List, Tuple, Optional

def process_data(data: List[int]) -> Tuple[int, int]:
    return (min(data), max(data))
    
def find_max(data: Optional[List[int]] = None) -> Optional[int]:
    if data:
        return max(data)
    return None



""" ___________________________________"""

x = 10
print(type(x))
x = "Hello"
print(type(x)) #dynamic typing


""" ___________________________________"""

def add(a: int, b: int)->int:
    if type(a) !=int:
        return "invalid"
    return a+b

""" ___________________________________"""


def mutation(lst):
    lst.append(10)
    return lst
    
my_nums = [1,2,3]
list_after_call = mutation(my_nums)

print(my_nums)
print(list_after_call)

#def mutation(lst=[]):#default parameter exexcutes only once
def mutation(lst=None):#default parameter exexcutes only once
    if lst == None
        lst =[]
    lst.append(10)
    return lst
    
""" ___________________________________"""

my_tuple = (10,20,3)
*x, z = my_tuple #*x takes all values apart from one that goes to Z


""" ___________________________________"""

for _ in range(10):
    print("hi")#anonimys var
    if (k == 100)
        break #if does not hit break then it goes into ELSE
else:
    pass #hit if not break from the loop

coordinate = [5,10]
x,_ = coordinate

""" ___________________________________"""

def get_data():
    for i in range(10):
        yield i
    
    yield -1
    
def process(data):
    print(data)
    
gen = get_data()

#use the variable as a result and a condition
while (data :=  next(gen)) != -1:
    process(data)



#or
results_walrus = [result for x in range(10) if (result := f(x)) >3]

""" ___________________________________"""

lst = [1,2,3,4]
numbersfunc(*lst)#passes 4 individual elements

hehe = {
    "key" :"5"
    "target": 10
}
parse_func(**hehe)



""" ___________________________________"""
#normal case
char_count = {}
string = "aaaabbbbcccsssbba"

for char in string:
    if char not in char_count:
        char_count[char] = 0
        
    char_count[char] +=1



from collections import defaultdict

def default():
    return 0

char_count = defaultdict(default)


#or
for char in string:
    wordcount[char]= wordcount.get(word,0) +1 #if no such instance, then gives default 0 value

#or

""" ___________________________________"""

import threading
lock = threading.Lock()

with lock:
    print("thread safe block")
    

""" ___________________________________"""
from contextlib import suppress

with suppress(FileNotFoundError)
    open("non_existent_file.txt")
    

""" ___________________________________"""
import tempfile

with tempfile.TemproraryFile(mode='w+t') as tmp:
    tmp.write("Temp data..")
    tmp.seek(0)#go back to the start of the file to read
    data = tmp.read()
    print(data)#temp file will be deleted after execution
    
    
 
""" ___________________________________"""
#custom context manager
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        print("Starting timer..")
        return self#optional
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type,exc_val,exc_tb)
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"Timer stopped {self.elapsed:.4f")
        
with Timer() as timer:#enter is called, self is returned as timer
    total = sum(range(100000))
    print("Sum calculated:", total)
    
    



""" ___________________________________"""
#define a simple metaclass
#defines how method CLASS is created
class AutoMethodMetaclass(type):
    def __new__(cls,name,bases,dct):
        def hello(self):
            print(f"Hello {self.__class__.__name__}")
        dct['hello'] = hello #add method to class dictionary
        
        #create the class using the superclass type
        return super().__new__(cls,name,bases,dct)
        

#this now has hello method by default
class MyClass(metaclass=AutoMethodMetaclass):
    def __init__(self,value):
        self.value = value
        
obj = MyClass(3)
obj.hello()

""" ___________________________________"""
#another example

class PluginMeta(type):
    registry = {}
    
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls,name,bases,attrs)
        
        #avoid registering the base class itself
        if bases != ():
            PluginMeta.registry[name] = new_class
            print(f"Registered plugin {name}")
        return new_class
        
class Plugin(metaclass=PluginMeta):
    def run(self):
        raise NotImplemnetedError
        
        
class AnalyticsPlugin(Plugin):
    def run(self):
        print("Run analutics")
        
for plugin_name, plugin_class in PluginMeta.registry.items():
    print(f"Instance {plugin_name}")
    plugin = plugin_class()
    plugin.run()
    

""" ___________________________________"""

def describe(obj):
    if isinstance(obj,int):
        print("this is int type")

from functools import singledispatch

@singledispatch
def describe(obj):
    raise NotImplementedError(f"Cannot describe {type(obj)}")

@describe.register
def _(obj:int):
    print("integer")

@describe.register
def _(obj:str):
    print("string")

""" ___________________________________"""
list1 = [1,2,3]
list2 = [54,2,3]
combined = [*list1, *list2]#adds individual elements into the list

""" ___________________________________"""
def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""
    
    local_scope={}
    exec(code,{}, local_scope)#second object is global scope
    print(local_scope["greet"]("Alice"))

""" ___________________________________"""
def demonstrate_eval():
    expression = input()#u typed print("Hello") or 3*7
    #result = eval(expression)#21
    
    #safe eval
    variables = {"a":2, "b":3,"c":4}
    result = eval(expression,{},variables)#a+b+c
    
    print(f"{result}")
""" ___________________________________"""
#doc string

def greet(person: str, age: int) ->str:
    """
    Greets a person by name and age.
    
    :param person: The name of the person (expected to be a string).
    :param age: The age of the person (expected to be an integer).
    :return: A greeting message (expected to be a string).
    """

    return f"Hello"
    
print(greet.__annotations__)

""" ___________________________________"""

people = [
    {"name": "Alice", "age":25},
    {"name": "Ali", "age":21},
    {"name": "Bob", "age":23}
]

people.sort(key=lambda person: person['age'])

for person in people:
    print(f"{person['name']}: {person['age']}")
    
""" ___________________________________"""
#ternary operator
age = 25
smokes = True
health = "Poor" if age > 60 or smokes else "Good" if age < 30 else "Fair"


""" ___________________________________"""
#unpacking
dict = {"a":2, "b":5}
q,w = dict.items()
q,w = dict.values()

#swap values

a= 4
f =5
f,a =a,f


#sort by key
lst = [[1,2],[4,5]]
lst.sort()# by first element in the list

lst.sort(key=lambda x: x[1])#by second element


import itertools
lst = [1,2,3,4,5]
sum_list = itertools.accumulate(lst) #1,3,6,10,15

lst2 = ['A', 'V', 'B','E']
chain_list = itertools.chain(lst,lst2)
print(list(chain_list))


names = ['Tim', 'Joe', 'Bill']
show = [1,0,1] #sets true and false
compressed_list = itertools.compress(names, show)
print(list(compressed_list))#if 0 then not printed

