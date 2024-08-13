class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    
    def multiplication(self):
        return self.a * self.b
    
a = int(input("Enter the Value of a: "))
b = int(input("Enter the value of b: "))

calc = Calculator(a,b)

print(calc.add())
print(calc.multiplication())    
    
