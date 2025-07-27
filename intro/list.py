  
lst = [1,2,3,4,5,6,7,8,9]
contains = 2 in lst
index = lst.index(2)
lst2 = lst[:]#copy list, different pointer to mem


n1 = [x for x in range(10) if x % 2 == 0]
n2 = [x for x in range(10) if x % 2 != 0]

zipped = list(zip(n1,n2))
zipped_2 = zipped[::-1]#reversed the list
zipped_2.extend(n2[::-1])#extend function adds elements from another list

n1[-5:-5] = [999]
n1[1:4] = ['a','b','c']

lst = sorted(n1, key=lambda x: (isinstance(x, int), x), reverse = True)




#append one list to another

numbers = [1,2,3]
numbers.extend(list([4,5]))
print(numbers)


people: list[str] = ['Mario', 'Elon', 'Gary', 'Elon', 'john']
print(people.count('ELon'))

people.insert(1, 'Luigi')

people.sort(key: lambda name: name.lower())
people.sort(key: lambda name: len(name))



#problem 1
items = [1,2,3]
items.insert(0,0)# O(n) time-complexity, not gud!
#fix
from collections import deque#const time insertion and removal

items = deque()
for i in range(10_000):
    items.appendleft(i)


#problem 2
values = [1,2,3,4,5,... , 1_000_000] # O(n) search
if 999_999 in values:
    pass
#fix
values = set(values)#const time insertion,deletion and lookup
if 999_999 in values:
    pass



#problem 3
"hello" + "!" # O(n) + O(m)

res = "" #immutable
for i in range(1,10001):
    res += str(i) + ","
    
#fix
parts =[]#mutable
for i in range(1, 10001):
    parts.append(str(i) + ",")#const time to append
res = "".join(parts)#turn list into a string
