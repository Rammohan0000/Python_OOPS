class Compare:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        
    def check_lists(self):
        while len(self.list1) == len(self.list2):
            for item in self.list1:
                if item in self.list2:
                    return "Both lists are Same"
                else:
                    return "List1 and List2 are not same"
            return "Please check the count for both lists" 
        
list1 = input("Enter the list1 elements:  ").split()
list2 = input("Enter the list2 elements: ").split()

compare = Compare(list1, list2)

print(compare.check_lists())
           
                
                    