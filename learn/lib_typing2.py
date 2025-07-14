#NOW, typing is getting deprecated in Python!

import typing as t
import collections.abc as c #new substitution to typing

#def say_hello(names: t.Iterable) -> None:
def say_hello(names: c.Iterable) -> None:
    for name in names:
        print(name)
        
say_hello(['Bob', 'Jack'])


#def repeat(func: t.Callable, times: int) -> None:
def repeat(func: c.Callable, times: int) -> None:
    for i in range(times):
        func()
        
def hello() ->None:
    print('Hello')
    
repeat(hello, times=3)
