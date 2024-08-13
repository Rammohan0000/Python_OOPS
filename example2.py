class Concatenate:
    def __init__(self, a):
        self.a = a

    def concat(self, times=5):
        # Convert 'a' to a string and concatenate it 'times' times
        return int(str(self.a) * times)

    def calculate_sum(self):
        n1 = self.concat(1)
        n2 = self.concat(2)
        n3 = self.concat(3)
        return n1 + n2 + n3

# Prompt the user to input an integer and store it in the variable 'a'
a = int(input("Input an integer: "))

# Create an instance of Concatenate with the input value
concat = Concatenate(a)

# Calculate the sum of n1, n2, and n3 and print the result
print(concat.calculate_sum())
