import intro05 as mx
import platform
from datetime import datetime, timedelta

x = datetime.datetime.now()
print(x.strftime("%B"))
today = datetime.today().strftime('%Y-%m-%d')# Get today's date

x = platform.system()
x = dir(platform)


import math
x = math.sqrt(64)




import json

#convert from JSON to dictionary
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#convert dictionary to JSON
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)





#regular expression
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)#Search the string to see if it starts with "The" and ends with "Spain":

#[]    A set of characters    "[a-m]"
#\    Signals a special sequence (can also be used to escape special characters)    "\d"
#.    Any character (except newline character)    "he..o"
#^    Starts with    "^hello"
#$    Ends with    "planet$"
#*    Zero or more occurrences    "he.*o"
#+    One or more occurrences    "he.+o"
#?    Zero or one occurrences    "he.?o"
#{}    Exactly the specified number of occurrences    "he.{2}o"
#|    Either or    "falls|stays"
#()    Capture and group

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)




try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
finally:
  print("The 'try except' is finished")


x = -1
try:
    if x < 0:
      raise Exception("Sorry, no numbers below zero")
      
    if not type(x) is int:
      raise TypeError("Only integers are allowed")
except Exception as e:
    print(e)
    
    
    
    
    
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
txt = f"I love {fruit.upper()}"




name = input()
print(f"Hello {name}")
name = input("Enter your name:")

