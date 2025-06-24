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
print(RPS['ROCK']
print(RPS.ROCK.value)#1
