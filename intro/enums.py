from enum import Enum, Flag, auto, enumerate


class Color(Enum):
    RED: str = 'R'
    GREEN: str = 'G'
    BLUE: str = 'B'

#print(Color('R'))#Color.RED
#print(Color.RED)#Color.RED
#print(repr(Color.RED))#<Color.RED: 'R'>
#print(Color.RED.name)#RED
#print(Color.RED.value)#R

def create_car(color: Color) -> None:
    match color:
        case Color.RED:
            print(f"Red car")
        case Color.GREEN:
            print(f"Green car")
        case Color.BLUE:
            print(f"Blue car")
        case _:
            print(f"No such color")


#create_car(Color.RED) #helps with validating the input

#flag allows combining
class Colour(Flag):
    RED: int = 1
    GREEN: int = 2
    BLUE: int = 4
    YELLOW: int = 8
    BLACK: int = 9

yellow_and_red: Color = Colour.YELLOW | Colour.RED
print(yellow_and_red)

for clr in yellow_and_red:
    print("This colour:", clr)

new_clr: Colour = Colour.RED

if new_clr in yellow_and_red:
    print("FOUND COLOUR!")

print("Combination value: ",yellow_and_red.value)#Combination value:  9
print("Combination: ",yellow_and_red)#Combination:  Colour.BLACK



#auto allows autoassigning values to enums
class Colr(Flag):
    RED: int = auto()
    GREEN: int = auto()#values using power of 2 since inheriting Flag class. if it was Enum, then normal indexing
    BLUE: int = auto()
    YELLOW: int = auto()
    BLACK: int = auto()
    ALL: int = RED | GREEN | BLUE | YELLOW | BLACK #returns the union of all -> sum of all values

print(Colr.RED.value)
print(Colr.GREEN.value)
print(Colr.BLUE.value)





class State(Enum):
    OFF: int = 0
    ON: int = 1
    
switch: State = State.OFF

match switch:
case State.ON:
    pass
case State.OFF:
    pass
case _:
    pass
    
    
    
    
    


#-_______________________________#
#need to provide indexing
my_list = ["apples", "pears", "bananas"]

count = 0
for element in my_list:
    print(element)
    if count == 1:
        pass
    
    count +=1
    
#or
for x in range(len(m_list)):
    print(my_list[x])
    if x == 1:
        pass


for index, element in enumerate(my_list):
    print(x,element)
