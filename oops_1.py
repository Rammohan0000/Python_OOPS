class Car:
    def __init__(self, color, make):
        self.color = color
        self.make = make
        
    def start_engine(self):
        print(f"The {self.color} {self.make} engine started ")
        
my_car = Car("red", "Toyota")
your_car = Car("blue", "Ford")

my_car.start_engine()
your_car.start_engine()        
