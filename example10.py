import math

class Circle:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    def distance(self):
        return math.sqrt((self.list2[0] - self.list1[0]) ** 2 + (self.list2[1] - self.list1[1]) ** 2)

# Input handling
list1 = list(map(int, input("Enter the values of x1 and y1 (separated by space): ").split()))
list2 = list(map(int, input("Enter the values of x2 and y2 (separated by space): ").split()))

# Creating an instance of the Circle class
circle = Circle(list1, list2)

# Printing the distance
print(circle.distance())
