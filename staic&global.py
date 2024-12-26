#global var
x = 1
def check():
    global x
    x= x+5
    print("Inside value is :",x)
check()    
print("outside value is: ",x)

#static var
class Counter:
    count = 0  # Static variable (class variable)
    @classmethod
    def increment(self):
        self.count += 1
        return self.count
print(Counter.increment()) 
print(Counter.increment())  


