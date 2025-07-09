from functools import singledispatch

@singledispatch
def sum(a,b):
    raise TypeError("Unsupported types.")

@sum.register(int)
def _(a: int, b:int) -> int:
    return a+b

@sum.register(float)
def _(a: float, b:float) -> float:
    return a+b

print(sum(1,2))
print(sum("a","d"))

