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
