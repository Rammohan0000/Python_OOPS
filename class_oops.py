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
   
# An abstract class that cannot be instantiated directly and is meant to be subclassed.
# It serves as a blueprint for other classes and can contain one or more abstract methods, which are methods declared without any implementation.
# abstract methods -> declared in abstract class and must be implemented by subclasses
# use @abstractmethod decorator from the abc module
# Polymorphism allows us to handle different objects uniformly, improving code flexibility and simplicity.
from abc import ABC, abstractmethod
class Animal(ABC): #Abstract Base Class
    @abstractmethod
    def make_sound(self):
        print("This is a generic animal sound") # default implementation
class Dog(Animal):
    def make_sound(self): # override with specific behavior
        super().make_sound() # optionally call the default behavior
        return "Bow!!Bow"
class Cat(Animal):
    def make_sound(self):
        return "Meow!!!"
dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())

#Abstact class vs Inheritance
#Abstract Class Use it when you have a common interface or behavior that all subclasses must implement.
#Example: An abstract Shape class that requires all subclasses (Circle, Square, etc.) to implement an area() method.
#Inheritance:
#Use it when a subclass can naturally extend or reuse the functionality of the parent class.
#Example: A Car class inheriting from a Vehicle class to reuse attributes like speed and methods like move().#

#__repr__ helps during debugging, it provides a string representation of the object 
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

book = Book("1984", "George Orwell", 328)

print(str(book))    # Output: '1984' by George Orwell, 328 pages
print(repr(book))   # Output: Book('1984', 'George Orwell', 328)

# An abstract class is a class that cannot be instantiated directly and is meant to be subclassed.
# It provides a common interface for its subclasses and can contain one or more abstract methods. 
# Abstract methods are methods declared without any implementation and must be implemented by subclasses.
# This is useful for defining a common interface that all subclasses must follow
# Use the @abstractmethod decorator from the abc module to declare abstract methods.
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def stop_engine(self):
        return "Car engine stopped"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

    def stop_engine(self):
        return "Motorcycle engine stopped"

# Instantiate objects of the subclasses
car = Car()
motorcycle = Motorcycle()

print(car.start_engine())        # Output: Car engine started
print(car.stop_engine())         # Output: Car engine stopped
print(motorcycle.start_engine()) # Output: Motorcycle engine started
print(motorcycle.stop_engine())  # Output: Motorcycle engine stopped
