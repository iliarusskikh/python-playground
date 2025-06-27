#lambda

add_1 = lambda x: x + 1

result = add_1(1)
print(add_1)



my_numbers = [1,2,3,4,6,6]

def square(x):
    return x ** 2
    
squares = list(map(square, my_numbers))
squares = list(map(lambda x: x ** 2, my_numbers))

print(squares)


evens = list(filter(lambda x: x %2 ==0, my_numbers))#if returns true - keeps the items

#key for sorted function

values = [(1,'b',"hello"), (2,'a',"world"), (3,'c',"ok")]
sorted_values = list(sorted(values, key = lambda x: x[1]))


from functools import reduce
numbers = [1,2,3,4,5]

#sums the list without initialiser
sum_of_numbers = reduce(lambda acc,x: acc+x, numbers)

#using reduce to find the max value
max_value = reduce(lambda acc,x: acc if acc>x else x, numbers)
