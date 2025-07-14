""" __________________________________________"""

#dictionary comprehensions
names = ['Ze', 'Do', 'Ra']
profs = ['Code', 'Doc', 'Teach']

my_dict = {}

for key, value in zip(names,profs):
    my_dict[key] = value
    
#or
for i in range(3):
    my_dict[names[i]] = profs[i]
    
    
#or
my_dict = {
key:value for (key,value) in zip(names,profs)
}

my_dict = {
names[i]:profs[i] for i in range(len(names))
}




my_dict = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

my_dict = {
(key + "man" if key != "Spider" else "Superman"):value for (key,value) in my_dict.items()
}




import random
import string


keys = ["id", "username", "password"]
users = ["keshamama", "KnotAbot", "spongiBOBO", "IAMBATMAN"]


data = [{key : (i if key == "id" else users[i] if key == "username" else "".join(random.choices(string.printable, k=8))) for key in keys} for i in range(len(users))]
print(string.printable)

#password = "".join(random.choices(string.printable, k=8))#convert list to string


my_dict2 = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

my_dict2.pop("Bat") #removes a specified key
my_dict2.popitem() #removes the last item from a dictionary

my_dict3 = {0: ['a','b'], 1: ['c','d']}
my_copy: dict = my_dict3.copy() #dictionaries are unique, but the references inside are not unique. When changing value, it changes in both. Deep copy required
#because list inside the dict

print(my_dict2.get("Spider"))# returns a key. if doesnt exist, returns none
print(my_dict2.get("Spided", 'Missing!'))# returns missing if none
print(my_dict2.getdefault("Spidy", '???'))# if none, sets default value to given key
my_dict2.clear() #removes all items


keys: list[str] = ["id", "username", "password"]
values: dict = =dict.fromkeys(keys)#creates a dict and sets none value to each key
#values: dict = =dict.fromkeys(keys, __value:'myvalue')

for k, v in my_dict2.items():
    print(k,v)



my_dict2 = {
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}

my_dict2 |= {"NewKey": "anothervalue"} #adds to a dictionary aka update


# original dictionary
input_dict = {
    'website': 'GeeksforGeeks',
    'topics': ['Algorithms', 'DSA', 'Python', 'ML']
}

# deep copy using the dict() constructor
result = dict(input_dict)
