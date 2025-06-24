#dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])
print(len(thisdict))
x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys()#gets the list of the keys

thisdict = dict(name = "John", age = 36, country = "Norway")

x = thisdict.values()#list of values

x = thisdict.items()#The items() method will return each item in a dictionary, as tuples in a list.

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.pop("model")

for x in thisdict.values():
  print(x)
  
for x, y in thisdict.items():
  print(x, y)
  
mydict = thisdict.copy()#copies, othervise its a reference a=b
mydict = dict(thisdict)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)#child

  for y in obj:
    print(y + ':', obj[y])
