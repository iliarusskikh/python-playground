#metaclasses help implementing overloading

class UppercaseMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        # Check all attributes (methods) in the class
        for attr_name, attr_value in attrs.items():
            # Only check callable attributes (methods)
            if callable(attr_value) and not attr_name.startswith('__'):
                if attr_name != attr_name.upper():
                    raise ValueError(f"Method '{attr_name}' must be in uppercase")
        return super().__new__(cls, name, bases, attrs)

# Example class using the metaclass
class MyClass(metaclass=UppercaseMethodMeta):
    def VALID_METHOD(self):
        return "This is a valid method"

    # This will raise an error because the method name is lowercase
    def invalid_method(self):
        return "This will cause an error"

# Create an instance and test
if __name__ == "__main__":
    try:
        obj = MyClass()
        print(obj.VALID_METHOD())
    except ValueError as e:
        print(f"Error: {e}")



#_________________________________________________________#

'''
class AutoMethodMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add a new method to the class
        attrs['say_hello'] = lambda self: f"Hello from {name}!"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=AutoMethodMeta):
    def __init__(self, value):
        self.value = value

# Test the class
if __name__ == "__main__":
    obj = MyClass(42)
    print(obj.say_hello())  # Automatically added method
    print(obj.value)
    
'''
