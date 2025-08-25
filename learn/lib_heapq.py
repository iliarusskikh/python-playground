import heapq

numbers = [1,8,3,7,5,2,9]

largest = heapq.nlargest(3,numbers)
print(largest)

smallest = heapq.nsmallest(3,numbers)
print(smallest)

