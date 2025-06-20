#generators

#vs iterator -> object to loop through the sequence of data

import sys

x = [1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(x))

for element in x:
    print(element)
    

for i in range(1,11):#not storing all list numbers
    print(i)


y = map(lambda i: i**2,x)
print(list(y))# y needs to be converted to list representation

for i in y:
    print(i)#sequence is generated as we loop through this

print(next(y))
print(y.__next__())

for i in y:#this will continue from next function
    print(i)#sequence is generated as we loop through this



while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break


x = range(1,11)
print(x)#range object is not an iterator
#iter()
#.__iter__()
print(next(iter(x)))

for i in iter(x):
    print(i)
    



#how to create your own iterator

class Iter:
    def __init__(self,n):
        self.n=n
    
    def __iter__(self):
        self.current = -1
        return self
    
    def __next__(self):
        self.current +=1
        if self.current >=self.n:
            raise StopIteration
            
        return self.current

x = Iter(5)

for i in x:
    print(i)
    
    
#now generators!
def gen(n):
    for i in range(n):
        yield i
        
for i in gen(5):
    print(i)


def gen2():
    yield 1
    yield 5
    yield 12
    yield 1
    yield 45







def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row
    
z = (i for row in open(file_name,"r"))
for l in z:
    print(l)
    
#gen comprehentions
x = (i for i in range(10))

for j in x:
    print(j)
