
class Microwave:
    def __init(self, brand: str, power_rating : str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave {self.brand} is turned on')
        else:
            self.turned_on = True
            print('Turned on!')

    def turn_off(self) -> None:
        if self.turned_off:
            print(f'Microwave {self.brand} is turned off')
        else:
            self.turned_on = False
            print('Turned off!')
    
    def __add__ (self,other):
        return f'{self.brand} + {other.brand}'
        
        

    
smeg : Microwave = Microwave(brand:'Smeg', power_rating:'B')
smeg1 = Microwave()
print(smeg.brand)





