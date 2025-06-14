f = open("myfile.txt", "x")#creartes new file
#"a" - Append - will create a file if the specified file does not exists
#W


with open("demofile.txt") as f:
  print(f.read())
#  print(f.read(5)) # 5 chars
#  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)#line by line
    
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
  
#w, overwrites file


import os
os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder")#folder delete



#reverse a string
txt = "Hello World"[::-1]# means start at the end of the string and end at position 0
print(txt)


