
mytuple = ("apple", "banana", "cherry") #unchangeable

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  
#the way you change tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

#unpack
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  

