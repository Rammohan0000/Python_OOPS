class Car:
    def __init__(self, maker, year):
        self.maker = maker
        self.year = year
    def get(self):
        return self.maker, self.year       
    def set(self, new_year):
        self.year = new_year
car = Car('hyundai', '2019')
print(car.get())
car.set('2025')
print(car.get()) 