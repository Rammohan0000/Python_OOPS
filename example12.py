class Last:
    def __init__(self, s):
        self.s = s
        self.count = 0
        
    def last_word(self):
        for char in reversed(self.s):
            if char != ' ':
                self.count += 1
            elif self.count > 0:
                break
            
        return self.count
    
s = str(input("Enter the sentence to find the length of last word: "))

last = Last(s)
print(last.last_word())           
                