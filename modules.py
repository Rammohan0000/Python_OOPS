# Module is file containing Python code (functions, classes, and variables) that can be imported and reused in other Python scripts or modules
#Encourages code reusability
#Provides built-in functionality with standard modules (e.g., math, os, random).

#save it with example_module.py
def add(a,b):
    return a + b

person1 = {
    "name":'john',
    "age": 25,
    "country":'USA'
}

#create a new python file, import the above python code using
#import example_module
#print(add(1,2))
#we can access variables also
#a = example_module.person1['age']
#print(a)

#renaming an module by using alias
#import example_module as em
#a = em.person1["name"]
#print(a)

#using *-> importing entire module
from math import *
print("Square root of 16:", sqrt(16))
print("Factorial of 5:", factorial(5))
print("GCD of 48 and 18:", gcd(48, 18))
print("LCM of 4 and 5:", lcm(4, 5))
print("2 raised to the power of 3:",pow(2, 3))
print("Ceiling of 4.3:", ceil(4.3))
print("Floor of 4.7:", floor(4.7))



