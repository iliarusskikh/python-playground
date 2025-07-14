#str

text: str = 'hello'
print(text.capitalize())#->Hello
 
text2: str = "HeLLo"
print(text.casefold())#->hello, convert to the same format as others for comparison

print(text.encode(encoding='UTF-8', errors='strict'))#if fails, then gives error, encoding to bianry
print(text.endswith('o'))#true/false

text3: str= 'text\ttext2\ttext3'
print(text3.expandtabs(20))

text4: str= 'Please find the string'
position:int = text4.find('the') #when using index instead, index would give error if not found
print(text4[position:])

text5: str = '{subject} is doing: {action}'
print(text5.format(subject='Cat',action='jump'))

coordinates: dict = {'x':10, 'y':-5}
text:str = 'Coordinates: ({x}, {y})'
print(text.format_map(coordinates))

text:str ='hello123'
print(text.isalnum())#if its alphabetic numeric string (no other characters)
#.isalpha()
#.isascii()
#.isdecimal, (also digit and numeric)
#.isdigit() 1,2,3,4,5,6,7,8,9
#.isnumeric()

#.islower()
#.isspace() if string contains spaces only

print("-".join(['text1','text2']))#text1-text2, joins using -

text:str = 'a+b=c'
print(text.partition('='))# ('a+b','=','c')

#text.replace('one', 'new', 1)#only to repalce 1 occurence
position = text.rfind('A')#finding first occurence from the right side


text.rsplit(sep=' ')

text.strip('WordToRemoveOrANTH')
