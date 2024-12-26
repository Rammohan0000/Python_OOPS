# shallow copy and deep copy -> means creating a new object and copying the content of the original object to the new object.
# shallow copy -> creates a new object and copies the reference of the original object to the new object. -> changes in the new object will reflect in the original object.
# deep copy -> creates a new object and copies the content of the original object to the new object. -> changes in the new object will not reflect in the original object.

import copy
list1 = list(map(int,input("Enter the list of numbers:").split()))
shallow_copy = copy.copy(list1)
shallow_copy[0] = 100
print("Shallow copy:", shallow_copy)
print("Original list:", list1)
deep_copy = copy.deepcopy(list1)
deep_copy[0] = 200
print("Deep copy:", deep_copy)
print("Original list after deep copy modification:", list)

