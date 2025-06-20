#comprehensions




""" __________________________________________"""
values = []

for x in range(10):
    values.append(x)
    
#too slow

values = [x for x in range(10)]#for loop inside of a list
#for every iteration value of x is taken and added to the list



""" __________________________________________"""

evens = []
for numbers in range(10):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
        
evens = [numbers for numbers in range(10) if number % 2 == 0]

""" __________________________________________"""

options = ["any", "albany", "apple", "world", "hello",""]
valid_strings = []

for string in options:
    if len(string) <=1:
        continue
    
    if string[0] !="a":
        continue
    
    if string[-1] != "y":
        continue
        
    valid_strings.append(string)
    
print(valid_strings)

valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]


""" __________________________________________"""
#nestred list comprehension

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)
        
flattened = [num for row in matrix for num in row]

        
""" __________________________________________"""
#categorize numbers  as even or odd

categories = []

for number in range(10):
    if number % 2 == 0:
        categories.append("Even")
    else:
        categories.append("Odd")
        
categories = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]


""" __________________________________________"""
#build a 3D list

import pprint

printer = pprint.PrettyPrinter()

lst = []

for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    
    lst.append(l1)

printer.pprint(lst)

lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]


""" __________________________________________"""
#list comp with funcs

def square(x):
    return x**2
    
squared_nums = [square(x) for x in range(10)]



""" __________________________________________"""
#creating a dictionary
pairs = [("a",1),("b",2),("c",3)]
my_dict = {k: v for k,v in pairs}
my_dict = {k: square(v) for k,v in pairs}


""" __________________________________________"""
#removing duplicates
nums = [1,2,3,4,5,5,5,5,6,8]
unique_squares = {x**2 for x in nums}#set sintax is { braces




""" __________________________________________"""
#generator comprehensions

sum_of_squares = sum(x**2 for x in range(100000))





