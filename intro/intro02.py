#sets

myset = {"apple", "banana", "cherry"}
# Set items are unchangeable, but you can remove items and add new items.

set1 = {"abc", 34, True, 40, "male"}

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
thisset.add("orange")


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")#error if no object

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")#no errors good method!

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()#removes random item


thisset = {"apple", "banana", "cherry"}
thisset.clear()#clears set

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
set3 = set1 | set2#same stuff


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)#only duplicates
set3 = set1 & set2 #same

set3 = set1.difference(set2)
set3 = set1 - set2 #same

set1.difference_update(set2)


