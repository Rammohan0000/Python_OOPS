class Difference:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    def set_difference(self):
        matches = []
        
        for item in self.list1:
            if item in self.list2:
                matches.append(item)
        
        if matches:
            return f"Matching items: {', '.join(matches)}"
        else:
            return "No matches found between list1 and list2"

# Input handling
list1 = input("Enter the set of colors for list1 (separate by spaces): ").split()
list2 = input("Enter the set of colors for list2 (separate by spaces): ").split()

# Creating an instance of the Difference class
diff = Difference(list1, list2)

# Printing the result
print(diff.set_difference())
