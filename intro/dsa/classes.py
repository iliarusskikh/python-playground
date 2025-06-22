class Guitar:
    def __init__(self):
        self.n_strings = 6
        #self.play()

    def play(self):
        print("papapa")
        
    
my_guitar = Guitar()

print(my_guitar)
#my_guitar.play()

class ElectroGuitar(Guitar):
    def __init__(self):
        super().__init__()
        self.n_srtings = 8
        self.color = "blue"
        self.__cost = 50#make it private
        
    def __secret(self):
        print("this guitar cost," self._Guitar__cost)
        
my_gita = ElectroGuitar()
print(my_gita._ElectricGuitar__cost)#still can reveal
