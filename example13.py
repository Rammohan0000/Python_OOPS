class Duplicate:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    def search_duplicate(self):
        matches = []
        for item in self.list1:
            if item in self.list2:
                matches.append(item)
        if matches:
            return len(matches)
        else:
            return "No matches found in list1 and list2"    
        
list1 = input("Enter the list1 of elements seperated by spaces: ").split()
list2 = input("Enter the list2 of elements seperated by spaces: ").split()

duplicate = Duplicate(list1, list2)
print(duplicate.search_duplicate())
               