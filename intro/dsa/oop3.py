import csv

class Item:
#class attribute
    pay_rate = 0.8 #20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        #validations
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero"#gives assertion error AssertionError
        
        #assign to self object, instance attribute
        self._name = name#or do __name
        self.price = price
        self.quantity = quantity
        
        #actions to execute
        Item.all.append(self)
        
    @property
    def name(self): #item1.name
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) >= 10
            raise Exception("Name is too long")
        else:
            self._name = value#item1._name = "Bob
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}')"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r')as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
             )
        

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
            
            
            
#    @property#cannot modify this
#    def read_only_name(self):
#        return "AAA"
            
    
        
    


"""
item1 = Item("Phone", 100,2)
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5

#print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 120
item2.quantity = 7

item2.newattr = False#add new attribute

print(item1.pay_rate)
print(Item.__dict__)#all attribute for class level
print(item1.__dict__)#all attributes for instance level

item2.pay_rate = 0.7 #modified at isntance level

for instance in Item.all:
    print(instance.name)


item3 = Item("Cable", 170,6)

"""

Item.instantiate_from_csv()

print(Item.all)

#Item.is_integer(6.6)

class Phone(Item):
    def __init__(self, name:str, price:float, quantity=0, broken_phone=0):
        super().__init__(name,price,quantity)
        self.broken_phone = broken_phone




#encapsulation
print(item1._name) #private modification

#abstraction
item1.send_email()#concealed processes

#inheritance

#polymorphism

name = "jim"
print(len(name))

somelist = ["some", "list"]
print(len(somelist))

