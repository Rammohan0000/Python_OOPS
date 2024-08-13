class Difference:
    def __init__(self, n):
        self.n = n
    def get_difference(self):
        if n <=17:
            return 17 - n
        else:
            return (n - 17) * 2
        
n = int(input("Enter the vlaue of n: "))

diff = Difference(n)

print(diff.get_difference())          
        