#pip install mypy static type analysis tool
# mypy C://myfolder/file.py
from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar


#x:str = 1 error detected

def add_numbers(a: int, b:int) ->int:
    return a+b
    
x = add_numbers(1,4)

#print(x)

#x: list[list[int]] = [] does not work as list is not a type however with typing

x: List[List[int]] = []

x: Dict[str,str] = {"a": "b"}

Vector = List[float]#usign own types

def foo(v: Vector) -> Vector:
    return v


def fow(output: Optional[bool]=False):
    pass

fow()#since its optional, function call can be called without parameters

def fqw(seq: Sequence[str]):
    pass

fqw(("a","b","c")) #tuple
fqw(["a","b","c"])#however, set is not a sequence, so cannot pass {1,2,3,4}, since no indexing available

#q: tuple = (1,2,4,"hello")
q: Tuple[int,int,int,str] = (1,2,4,"hello") #each element needs to be specified


#callable - function as a parameter, FAAP

def ffg(func : Callable[[int,int],str]):# that callable function should have 2 int parameters, and str return type
    func(1,2)

def add(x:int, y:int) -> int:
    return "hello"

ffg(add)


#TypeVar

T = TypeVar('T')
#basically template from c++
def get_item(lst:List[T], index: int) -> T:
    return lst[index]
    

#NOW, typing is getting deprecated in Python!

