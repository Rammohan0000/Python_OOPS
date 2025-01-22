#  allows a class to have more than one method with the same name, as long as their parameter lists are different. 
# method overloading is compiler time polymorphism
class MathOperations:
    def add(self, a, b, c):
        return a + b + c
math_operation = MathOperations()
print(math_operation.add(1, 2, 3))
print(math_operation.add(4, 5, 6)) 

# 2nd example
class Example:
    def display(self, a=None, b=None):
        if a is not None and b is not None:
            print(f"Two arguments: {a}, {b}")
        elif a is not None:
            print(f"One argument: {a}")
        else:
            print("No arguments")
obj = Example()
obj.display()
obj.display(10)
obj.display(10, 20)



