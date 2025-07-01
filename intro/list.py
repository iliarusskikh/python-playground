  
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
