class Count:
    def __init__(self, numbs):
        self.numbs = numbs
        
    def list_count(self):
        count = 0
        
        for num in self.numbs:  # Use self.numbs to refer to the instance variable
            if num == 4:
                count += 1
                
        return count  # Return the count after the loop finishes

# Input handling: Convert the input string to a list of integers
numbs = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

# Create an instance of Count
count = Count(numbs)

# Print the count of the number 4 in the list
print(count.list_count())
