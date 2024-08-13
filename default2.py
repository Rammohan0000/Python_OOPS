class Car:
    def __init__(self):
        self.color = "Black"
        self.maker = "Venue"
        
    def getinfo(self):
        print(f"Car details: {self.color} , {self.maker}")
        
car = Car()
car.getinfo()            
        