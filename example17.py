class Verification:
    def __init__(self, input_list):
        self.input_list = input_list
        
    def check(self):
        if len(self.input_list) == 0:
            return "Please check the input form"
        
        for i in range(len(self.input_list) - 1):
            if self.input_list[i] == self.input_list[i + 1]:
                return "Duplicate Values"
        
        return "No more Duplicate Values"

# Take user input and split into a list
input_list = input("Enter the values of the list separated by spaces: ").split()

# Instantiate the Verification class
verification = Verification(input_list)

# Call the check method and print the result
print(verification.check())
