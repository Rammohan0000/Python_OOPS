class Ascending:
    def __init__(self):
        self.list = [1,2,3,4,2]
        
    def sorted_asc(self):
        for i in range(len(self.list) - 1):
            if self.list[i] > self.list[i + 1]:
                return False
        return True    
                
asc = Ascending()
print(asc.sorted_asc())                