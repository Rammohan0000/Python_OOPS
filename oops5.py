class Car:
    def __init__(self, color, model, year):
        self.__color = color  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year    # Private attribute

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def accelerate(self):
        print("Car accelerating")

# Create an instance of the Car class
my_car = Car("Red", "Toyota Corolla", 2020)

# Call methods on the Car instance
my_car.start()        # Output: Car started
my_car.accelerate()  # Output: Car accelerating
my_car.stop()        # Output: Car stopped

# Get and set color
print(my_car.get_color())  # Output: Red
my_car.set_color("Blue")
print(my_car.get_color())  # Output: Blue
