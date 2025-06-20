class Point:
    x: int
    y: int
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
        
    def __eq__(self, other)
        return self.x == other.x and self.y == other.y
        
        
        
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    class_var: ClassVar[int] = 100 #wrapper will ignore this variable as its a class var
    
p1 = Point(1,2)
p2 = Point(2,1)
print(p1,p2)
print(p1==p2)




class Rectangle:
    def __init__(self,height, width):
        self.height = height
        self.width = width
        
@dataclass
class Square(Rectangle):
    side: float
    
    def __post_init__(self):
        super().__init__(self.side, self.side)#we need to write manually when inheriting from non dataclass base class
        
        
        
@dataclass
class Rectangle1:
    height: int
    width: int
        
@dataclass
class Rec2(Rectangle1):
    color: str

rect = Rec2(10,10,"green")




#passing the parameter

from dataclasses import InitVar

@dataclass
class C:
    i: int
    j: int | None = None
    database: InitVar[str | None] = None
    
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')
            
c = C(10, database={"j":"value"})
