age = 23
name = "Tim"

print("my name ",name,"my age", age, "years old", sep="|")
print("hellow world", end="|")
print("hello") # same line


help(print)#documentation for a name or doc strings """ """


rng = range(10) #(2,10,2)
print(list(rng))
print(rng)#returns iterator

strings = ["my", "world", "apple"]
lengths = map(len, strings)#length of all items, len built in function applied to each element
print(list(length)) #converts iterator into a list of results

lengths = map(lambda x: x+"s", strings)


def longer_than_4(string):
    return len(string) > 4
    
filtered = filter(longer_than_4,strings)
print(list(filtered))
filtered = filter(lambda x:len(x)>4,strings)

numbers = [1,2,4,5,3,1]
print(sum(numbers))
print(sum(numbers, start=10))#gives initial value

sorted_nums = sorted(numbers)
sorted_nums = sorted(numbers, reverse=True)

people = [
    {"name": "Alice", "age":38},
    {"name": "Bob", "age":31},
    {"name": "Helen", "age":31},
    {"name": "Alex", "age":35}
]

sorted_nums = sorted(people,key = lambda person:person["age"])#sorted by age



tasks = ["write report", "attend meeting", "review code", "submit timesheet"]

for index, task in enumerate(tasks):
    print(f"{index + 1}, {task}")
print(list(enumerate(tasks)))


priorities = [2,4,5,1]
combines = list(zip(tasks,priorities))
for tasks, priorities in combines:
    print(f"{tasks} with {priorities") #excludes exessive elements, min length




#open function
file = open("test.txt", "w")#modes
file.write("Hello world! \n")
file.close()

#OR
with open("test.txt","w") as file:
    file.write("here")#auto closes the file
    
with open("test.txt","r") as file:
    mytext = file.read()#auto closes the file

with open("test.txt","ra") as file:#append
    file.write("mroe text")#auto closes the file

