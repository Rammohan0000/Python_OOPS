class Animal:
    def sound(self):
        print("Sound")
class Dog(Animal):
    def sound(self):
        print("Woof!")
class Cat(Animal):
    def sound(self):
        print("Meow!")                
        
animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()        