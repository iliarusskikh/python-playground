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
