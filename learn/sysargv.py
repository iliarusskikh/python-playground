#
import sys

print(sys.argv)

def function1(file):#file
    print('First func -f')
    print(file)


def function2(file):#file
    print('Second func -s')
    print(file)
    
def function3(file):#file
    print('Third func: only file name')
    print(file)
    
    
arguments = sys.argv[1:]#to start from the argument, skipping 0 term of the name of thefile


#***************************************#
#if len(arguments) != 1:
#    print(f"Error: 1 argument expected, {len(arguments)} received!")
#    sys.exit()
#    
#else:
#    argument = arguments[0]
#    if argument == 'f' or argument == 'first':
#        function1()
#    elif argument == 's' or argument == 'second':
#        function2()
#    else:
#        print(f"Error: Unacceptable argument, '{argument}' received!")
#        sys.exit()
#***************************************#
    
    
#***************************************#
#if len(arguments) != 2:
#    print(f"Error: 2 argument expected, {len(arguments)} received!")
#    sys.exit()
#else:
#    option = arguments[0]
#    filename = arguments[1]
#    
#if option == 'f':
#    function1(filename)
#elif option == 's':
#    function2(filename)
#else:
#    print(f"Error: Option not available, '{option}' received!")
#    sys.exit()
#***************************************#

#if len(arguments) < 1:
#    print(f"Error: At least 1 argument expected, {len(arguments)} received!")
#    sys.exit()
#else:
#    for arg in arguments:
#        if arg not in ('f','s'):
#            print(f"Error: {arg} not avaliable!")
#        elif arg == 'f':
#            function1()
#        else:
#            function2()
 
#***************************************#


try:
    filename = sys.argv[1]
except:
    print('Error: no filename!')
    sys.exit()

options = sys.argv[2:]
#python file.py text.txt -s -f

if options:
    for option in options:
        if option not in ('-f', '--first', '-s', '--second'):
            print(f"Error: {option} not available!")
            sys.exit()
    
    for option in options:
        if option == '-f' or option == '--first':
            function1(filename)
        elif option == '-s' or '--second':
            function2(filename)
            
else:
    function3(filename)
