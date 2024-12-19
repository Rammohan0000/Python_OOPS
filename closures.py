# closure -> Retains variables from the enclosing scope
# Used for callbacks, decorators, and encapsulation.
# Closures are created when a nested function references variables from its outer function.
# structure of closure is as follows
# An outer function defines variables and a nested inner function.
# The inner function uses variables from the outer function.
# The outer function returns the inner function.
# When a closure is created, Python internally stores a reference to the environment (variables in the enclosing scope) where the closure was defined. 
# This allows the inner function to access those variables even after the outer function has completed.
# Closures help encapsulate functionality. 
# The inner function can access variables from the outer function, but those variables remain hidden from the outside world.

def outer_function(message):
    def inner_function():
        print(f"Message: {message}")
    return inner_function
# Create a closure
closure = outer_function("Hello, Python!")
# Call the closure
closure()
# outer_function creates the variable message and defines inner_function, which uses message.
# Even though outer_function has finished execution, inner_function retains access to message.

# Example for Functionality Encapsulation
def multiply_by(n):
    def multiplier(x):
        return x * n
    return multiplier
# Create closures
double = multiply_by(2)
triple = multiply_by(3)
print(double(5)) 
print(triple(5)) 

# sorting with closures
def make_sort_key(key):
    def sort_function(item):
        return item[key]
    return sort_function
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]    
sort_by_age = make_sort_key("age")
sorted_data = sorted(data, key=sort_by_age)
print(sorted_data)

# increment counter
def counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count  # Access the `count` variable from the enclosing scope
        count += step
        return count
    return increment
counter1 = counter(10)
print(counter1())  # Output: 11
print(counter1(2)) # Output: 13
print(counter1(5)) # Output: 18
counter2 = counter()
print(counter2())  # Output: 1
print(counter2(3)) # Output: 4
