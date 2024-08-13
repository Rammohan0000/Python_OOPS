class Sum:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def get_sum(self):
        if a != b and b != c and a != c:
            return a + b + c
        else:
            return (a + b + c) * 3
        
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

sum = Sum(a, b, c)

print(sum.get_sum())             