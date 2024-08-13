class Car:
    def __init__(self, color, model, year):
        self.__color = color
        self.__model = model
        self.__year = year
        
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def start(self):
        print("Car Started")
    def stop(self):
        print("Car Stopped")
        
my_car = Car("Red", "Toyota", 2020)
my_car.start()
my_car.stop()
    
print(my_car.get_color())
my_car.set_color("Blue")

print(my_car.get_color())                
    