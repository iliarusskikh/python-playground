from typing import Final
from datetime import datetime
from typing import Self


VERSION: Final[str]  = '1.0.12' #cannot be changed

def show_date() -> None:
    print(datetime.now())


class Car:
    def __init__(self, brand:str, horsepower: int) ->None:
        self.brand = brand
        self.horsepower = horsepower
        
    def drive(self) -> None:
        print(f'{self.brand} is driving!')
        
    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}'
        
    def __add__(self, other: Self) -> str:
        return f'{self.brand} & {other.brand}'
        
        
        
volvo : Car = Car('volvo', 200)
print(volvo.brand)

volvo.drive()
print(volvo)

bmw : Car = Car('bmw', 300)
print(volvo + bmw)


