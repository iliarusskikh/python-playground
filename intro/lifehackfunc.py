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
