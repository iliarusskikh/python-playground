day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:#default value
    print("Looking forward to the Weekend")
  case 1 | 2 | 3 | 4 | 5:
    pass
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    pass


#keyword only arguments
def my_function(*, x):
  print(x)

my_function(x = 3)


x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


#lists are used as arrays
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)
  
cars.append("Honda")
cars.pop(1)#delete second element
cars.remove("Ford")#only first occurence

