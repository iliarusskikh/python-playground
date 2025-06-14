
print("Hello world!")

x = float(3) #casting 3.0
print(type(x))

x,y,z = 1,2,3
fruits = ["apple","orange","peach"]
x,y,z = fruits

x = dict(name="John", age=36)
x = list(("apple", "banana", "cherry"))

import random
print(random.randrange(1, 10))

for x in "banana":
  print(x)

a="banana"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt) #true false, if not in ...

b = "Hello, World!"
print(b[2:5]) # :5 from the start, 2: to the end

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
print(a.replace("H", "J"))

print(a.split(",")) # returns ['Hello', ' World!']

txt = "We are the so-called \"Vikings\" from the north."
# \xhh hex value

x = 200
print(isinstance(x, int))


