#mutable vs immutable

#immutable cannot be changed once defined
# str, int, float, bool, bytes, tuple

#mutable - list, set, dict

x = (1,2)
#x[0] = 1 #error!

z  = [1,2]
y = z
z[0] = 100
print(x,y) #prints 100 since list holds a ref.


def get_largest_nul(numbers, n):
    numbers.sort()
    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]

print(nums)
largest = get_largest_nul(nums,2)
print(nums)


#list comprehensions
x = [i for i in range(10)]
print(x)
x = [[j for j in range(5)] for i in range(10)]
print(x)
x = [i for i in range(10) if i % 2 ==0]
print(x)


def complicated_func(x,y, *args)
    pass
    
complicated_func(x=1,y=4,3,3,1,1,1,1,2,)#*args any number of positional arguements

def complicated_func2(**kwargs)
    print(kwargs["b"])
    
complicated_func2(x=1,s="hello",b = True)#key-word arguements stored within dictionary


def complicated_func3(a,b,c = True, d=False)
    pass
    
complicated_func3(*[1,2],**{"c": "hello", "d":"bye"})#reversed logic




#GIL global interpreter lock
#only one thread at a time to be executed
#since this thread requires to aquire lock on interpreter.

