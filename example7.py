class Check:
    def __init__(self, word):
        self.word = word
        
    def is_vowel(self, char):
        return char in self.word
    
word = 'aeiouAEIOU'

char = 'z'

check = Check(word)

print(check.is_vowel(char))    
                   