class Car:
    def __init__(self, brand: str, id:int) -> None:
        self.brand = brand
        self.id = id
        
    def __eq__(self,other) -> bool:
        return (self.id == other.id) && (self.brand == other.brand)
        
volvo: Car = Car('Volvo', 0)
toyota: Car = Car('Toyota', 1)

volvo2: Car = Car('Volvo', 0)

print(volvo == toyota)#false
print(volvo == volvo2)#false because it compares id of the objects

#_______________________________________________________#

for i in range(3):
    print(i)
else:
    print("all completed!")
    

#_______________________________________________________#
i: int = 1000

for i in range(3):
    print(f'for loop: {i}')

print(i)#get overwriten

#_______________________________________________________#

numbers: list[int|str] = [1,2,3,4,5,6,7,8,9]
numbers[2:4] = 100,200#replaces one section with a new section

#_______________________________________________________#
#do not use mutable defaults when creating a function, as it has same address for all instances.
def add_to_list(item: str, target: list[str] = []) -> list[str]:
    target.append(item)
    return target
    
def add_to_list2(item: str, target: list[str] | None = None) -> list[str]:
    if target is not None:
        target.append(item)
        return target
    
    return [item]

l1: list[str] = add_to_list('Bob')
add_to_list('James',l1)
print(l1)

l2: list[str] = add_to_list('Sandra')#it wouldnt create a new list but appent to existing one

