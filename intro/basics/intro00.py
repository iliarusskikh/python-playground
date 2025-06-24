
thislist = ["apple", "banana", "cherry"]# can have duplicates
print(thislist)
list1 = ["abc", 34, True, 40, "male"]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets


#List is a collection which is ordered and changeable. Allows duplicate members.

#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

#Dictionary is a collection which is ordered** and changeable. No duplicate members.

print(thislist[1])
print(thislist[0:2])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.insert(2, "watermelon")
thislist.append("orange")#adds at the end

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)# append from another list

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")#first occurence removed

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

newlist = [x for x in fruits]

thislist.sort(reverse = True)



def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)#or copy
mylist = thislist[:]


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
list3 = list1 + list2


