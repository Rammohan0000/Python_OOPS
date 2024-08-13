class Triplet:
    def __init__(self, input_list):
        self.input_list = [int(x) for x in input_list]  # Convert input to integers
        
    def find_triplet(self):
        self.input_list.sort()  # Sort the list
        triplets = []
        
        for i in range(len(self.input_list) - 2):
            if i > 0 and self.input_list[i] == self.input_list[i - 1]:
                continue
            left, right = i + 1, len(self.input_list) - 1
            
            while left < right:
                current_sum = self.input_list[i] + self.input_list[left] + self.input_list[right]
                
                if current_sum == 0:
                    triplets.append([self.input_list[i], self.input_list[left], self.input_list[right]])
                    
                    while left < right and self.input_list[left] == self.input_list[left + 1]:
                        left += 1
                         
                    while left < right and self.input_list[right] == self.input_list[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif current_sum < 0:
                    left += 1
                    
                else:
                    right -= 1
                    
        return triplets   

# Take input from the user and convert it to a list of integers
input_list = input("Enter the list of elements separated by spaces: ").split()

# Instantiate the Triplet class
triplet_finder = Triplet(input_list)

# Call the find_triplet method and print the result
print(triplet_finder.find_triplet())
