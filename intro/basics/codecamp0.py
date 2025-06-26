import random
import math
from enum import Enum

meaning = 41
#ternary operator
#print('Hello') if meaning >20 else print('not todau')


""" ____________________________________________________ """

first = "Name Bob"
#print(isinstance(first,str))

pizza = str("Pepperioni")


first = "Dave"
last = "Johns"
fullname = first + " " + last
fullname += "!"

decade = str(1980)
#print(type(decade))#string
statement = " " +decade
multiplelines = '''
Hey buddy

'''

sentence = 'I \'m back at work! \t WORK!\n\n Where\'s tjis at\\located'


#string methods
#print(first.lower())#only changed for print out
#.title() capitalises first letter of each word
#.replace("good", "ok) good with OK
#.len(statement)
#.strip() ->removes whitespaces lstrip, rstrip


#.center(20,"=")
#.ljust(16,".")+ $1.rjust(4)  .......... $1

#.startswith("D")
#.endswith("z")

price = 100

#.abs(100)
#.round(123.4)# to the nearest integer
#.round(123.4, 1) # to the nearest decimal


""" ____________________________________________________ """
#value = input("Please input..")


choice = random.choice("123")#choose one of the characters
ch = int(choice)


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
#print(RPS(2))
#print(RPS['ROCK']
#print(RPS.ROCK.value)#1



#lsit and tuples
list12 = ['Dave', True, 42]

#print("Dave" in list12)
print(list12.index('Dave'))
#len(list12)
#list12.append('NewItem')
#list12 += ['Hold'] # need sqr br otherwise it would add each char

list12.extend(['Robert', 'Jason'])#adds another list

list12.insert(0,'Bob')#add to specific position
list12[2:2] = ['Eddie', 'Alex']#adding new values, not replacing
list12.remove('Bob')
#.pop() removes last value in a list + returns this item

list12.sort()
list12.sort(key=str.lower) #this would include lower cases in the sorting algo

del list12[0] #removed item
list12.clear() #keeps the list but clears its content
del list12 #delete entire list

nums = [1,2,5,67,2,4,6,7]
nums.reverse()
nums.sort(reverse=True)

#print(sorted(nums, reverse=True))# does not modifies the list

#make a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

#tuple - unchangable data
mytup = tuple(('Dave',43,True))
anothertup = (1,3,5,6)
newlist = list(mytup)
newlist.append('NewValue')
newtuple = tuple(newlist)

(one,two, *three) = anothertup #unpacking

#.count(1) -> how many occurences



#dictionaries
dict = {
    "vocals": "Plant",
    "guitar": 2
}

band = dict(vocals="Plant", guitar="Page")
#len()
#band["vocals"]
#band.get("guitar")
#band.keys()
#band.values()
#band.items()  -> as tuples
#print("guitar in band) true/false

#band["vocals"] = "Cover"
#band.update({"bass":"JPJ"})
#band.pop("bass")
#band.popitem() -> remvoves last added item

#del band["drums"]
#band.clear()
#del band

#copy dict
band2 = band.copy() #different refs
band4 = dict(band)

#nested dict
member1 ={
    "name" : "Plant",
    "instrument": "vocals"
}

member2 ={
    "name" : "Page",
    "instrument": "guitar"
}

band6 = {
    "member1": member1,
    "member2": member2
}

#print(band6["member1"]["name"])




#sets -> no duplicates are allowed

numss2 = {1,2,3,4,5}
numss = set((1,2,3,4))

#add new elements
numss.add(7)
numss2.update(numss)#append more elements

#merge 2 sets to create a new set

numb2 = {1,2,3,4,5}
numb1 = set((7,8,5,3,1))

newset = numb.union(numb2)

#keep only the duplicates
numb2.intersection_update(numb)

#keep except duplicates
numb2.symmetric_difference_update(numb)


""" ____________________________________________________ """
#loops

value =  1
while value < 10:
    value +=1
    if value == 10:
        break
else:#occur when the loop is done. to avoid it, use break
    print("new value")
    

naame = ['Dave', True, 42]

for x in naame:
    pass
    

for x in range(4):
    pass
    
naames = ['Hehe', 12, 'Dodo']


""" ____________________________________________________ """
#functions

def hello(num1,num2):
    if (type(num1) is not int or type(num2) is not int):
        return
    print("Hello World")
    

""" ____________________________________________________ """
#recursion
def add_one(num):
    
    if(num >= 9):
        return num +1
        
    total = num + 1
    
    return add_one(total)
""" ____________________________________________________ """
#scope
#global
#nonlocal

player = {'person':'Dave', 'Coins':4}
message = "\n{person} has {coins} coins left.".format(**player)
# f"{num:.2f}"

#modules
#print(dir(random)


def hello(name, lang):
    greetings = {
        "English": "Hello",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
    
if __name__ == __main__:
    import argparse
    
    parser = argparse.ArgumentParser(
        description = "Provides a personal greeting."
     )
     
     parser.add_argument(
        "-n", "--name", metavar = "name",
        required = True, help= "The name of the person to greet."
     )
     
     args = parser.parse_args()
     
     msg = f"Hello {args.name}!"
     print(msg)

     parser.add_argument(
         "-l", "--lang",metavar = "language",
         required = True, choices["English", "German"],
         help = " The language of the greeting."
     )
     
     args = parser.parse_args()
     
     hello(args.name, args.lang)
     
#python hello.py -n "Dave" -l "German"
     
""" ____________________________________________________ """
#lambda

squared = lambda num: num * num
#print(squared(2))

sum = lambda a,b: a+b
#print(sum(3,5))


def func1(x):
    return lambda num: num+x
    
addTen = func1(10)#define num

print(addTen(4))#10+4 #pass x


lambda num: num * num
nums = [1,2,3,4,6,7,8]

squared_nums = map(lambda num: num * num, nums)#iterates over each element and applies function to it
print(list(squared_nums))



#filter function
odd_nums = filter(lambda num: num % 2 !=0, nums) #filter returns items that only produce a TRUE result.


from functools import reduce

total = reduce(lambda acc, curr: acc + curr, nums, 10) #equivalent to SUM function, providing an initial value as a third parameter
#lambda acc, curr: acc + len(curr)


""" ____________________________________________________ """
#exception handling

try:
    print(zz)
    if not type(zz) is str:
        raise TypeError("Only strings are allowed")
        raise Exception("Custom exception")
#except NameError:
except Exception as e:
    print(f"Error handled:{e}")
    
""" ____________________________________________________ """
#pip
#python -m venv .venv
#source .venv/Scripts/activate
#pip list

#pip install python-dotenv
#pip install -U pip && pip install -r requirements.txt

from dotenv import load_dotenv
import os

load_dotenv()

varkey = {os.getenv("API_KEY")}
# weatherdata = requests.get(url).json()


    

