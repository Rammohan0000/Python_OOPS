class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add_sqaure(self):
        return (lambda x, y: (x + y) **2)(self.x, self.y) 
    
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

square = Square(x, y)

print(square.add_sqaure())       