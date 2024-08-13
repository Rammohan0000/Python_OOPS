class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name")

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing private attributes through getter methods
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

# Modifying private attributes through setter methods
person.set_name("Bob")
person.set_age(25)

# Accessing updated private attributes
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 25

# Attempting to directly access private attributes (will raise an AttributeError)
# print(person.__name)  # AttributeError
