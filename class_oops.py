#class is blueprint of objects, it defines attributes and methods
# object is instance of class, that has state and behaviour associated with it
# the __init__() function it always executed when class is being initiated, it is used to assign values to object
#The self keyword in Python is used as a reference to the current instance of a class. It allows access to the instance's attributes and methods, It doesnot need to be named as self, but it has to be first parameter for any function of a class

class Cricket():
    def __init__(self, name, role):
        self.name = name
        self.role = role
cricket = Cricket("kl_rahul","batsmen")
print(cricket.name)
print(cricket.role)        

#__str__() provides a custom, human-readable description of an object
class Car():
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.model} is manufactured in {self.year}"
car = Car("venue",2019)
print(car.model)
print(str(car))

#method is a function that is defined within a class and is associated with an object. Methods operate on the data (attributes) of the object and provide behavior to the class.
#1.Instance Method -> Operate on individual instances of the class. They have access to both the instance (self) and class attributes.
class Cricket():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def player_info(self):
        return f"the player name is {self.name} and his age is {self.age}"
cricket = Cricket("kl_rahul",33)
print(cricket.player_info())        
        
#2.class Methods -> Operate on the class itself, not on individual instances. They have access to the class through the cls parameter.
#Use the @classmethod decorator.
# Useful when you need to modify class-level data.
class Car:
    car_name = "Hyundai"
    @classmethod
    def change_car(cls,new_name):
        cls.car_name = new_name
print(Car.car_name)
Car.change_car("mahindra")
print(Car.car_name)     

#3.Static Methods ->Do not operate on an instance or class and don’t require self or cls. 
# They are utility functions that belong to the class for logical grouping.
# Use the @staticmethod decorator.
#  Useful for utility functions that are relevant to the class but do not depend on instance or class data.
class MathUtils:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
# Using the static method
print(MathUtils.add(5, 3))  # Output: 8

#4.Special Methods ->Built-in methods in Python that start and end with double underscores (__). 
# They allow customization of class behavior.
#Used for operator overloading, object representation, and more.
class Car():
    def __init__(self,model,year):
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.model} is manufactured in {self.year}"
car = Car("venue",2019)
print(car.model)
print(str(car))

#modify object properties
car.year = 2025
print(str(car))

#delete object property
#del car.year
print(str(car))# getting error i.e., year is missing

#delete object
#del car
print(str(car))

#class statement cannot be empty , if it is need to empty use "pass" keyword
class Cricket:
    pass