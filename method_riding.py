# Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass. 
# method overriding is run time polymorphism
class Cricket_ODI:
    def Batsmen(self):
        print("Pavan is Best Batsmen")
class Cricket_T20:       
    def Batsmen(self):
        print("Vinay is Best Batsmen")
class Cricket_Test:        
    def Batsmen(self):
        print("Sai is Best Batsmen")
        
odi = Cricket_ODI()
t20 = Cricket_T20()
test = Cricket_Test()

odi.Batsmen()
t20.Batsmen()
test.Batsmen()



           
            
            
        