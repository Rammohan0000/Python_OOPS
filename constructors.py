#constructors are special methods used to initialize objects of a class
#The primary constructor in Python is the __init__() method
#1.Default Constructor -> A constructor with no parameters (other than self).
class Cricket():
    def __init__(self):
        self.name = 'kl_rahul'
        self.age = 34
cricket = Cricket()
print(cricket.name,cricket.age)    

#default constructor -> no self and __init__ initialized by python compiler implicitily
class KoKo:
    pass
k = KoKo()
print(k)

#2.Parameterised Constructor ->  accepts arguments to initialize instance attributes
class Football():
    def __init__(self,name,role):
        self.name = name
        self.role = role
football = Football('bigil','30')
print(football.name, football.role)     

#3.Non-Parameterised Constructor -> A user-defined constructor (__init__ method) that does not take any parameters except self.
#It initializes the object with predefined values or performs specific tasks during object creation.
#explicitly defined
class Carrom:
    def __init__(self):
        self.role = 'defender'
c = Carrom()
print(c.role)        

#inheritance ->allowing a class to acquire the properties and methods of another class
#1.Single level inheritance -> single class inherits from single parent class
class Car():
    def run(self):
        print("This needs power to move")
class Electric(Car):
    def power(self):
        print("This moves by electric power")
e = Electric()
e.power() # child class
e.run() # parent class

#2.Multilevel inheritance -> A child class inherits from a parent class, and then another child class inherits from this child class (creating a chain).
class Car:
    def Engine(self):
        print("this needs some power to move")
class Fuel(Car):
    def combustion(self):
        print("this runs by petrol")
class Electric(Fuel):
    def replace(self):
        print("lot of fuel cars replaced by EV")              
electric = Electric()
electric.Engine()
electric.combustion()
electric.replace()

#3.Multiple inheritance -> A child class inherits from more than one parent class
#Can lead to complexity and ambiguity in method resolution

class P1:
    def display1(self):
        print("This P1 reporting!!!")
class P2:
    def display2(self):
        print("This P2 reporting!!!")
class P3(P1,P2):
    def display3(self):
        print("This is P3 reporting!!!")                
p = P3()
p.display1()
p.display2()
p.display3()








