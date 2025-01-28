color_list=["Red", "Blue", "Green", "Black"]
print(color_list)

color_list.insert(2, "White") #Insert an item at third position
print(color_list)

color_list.remove("Black")
print(color_list)
                                                                        
color_list[2]="Yellow"
print(color_list)

color_list.pop(2)
print(color_list)

color_list.index("Red")
color_list.count("Blue")

color_list.sort(key=None, reverse=False)
print(color_list)

color_list.sort(key=len, reverse=True)
print(color_list)

color_list.reverse()
print(color_list)

#convert_list_into_tuple
lst = [1,2,3,4]
tuple = tuple(lst)
print(tuple)

color_list.clear()
print(color_list)

#[::] specify start,stop and step
mylist = [1,2,3,4,5,6,7,8,9]
sublist = mylist[2:8:2]
print(sublist)

sublist = mylist[8:2:-2]
print(sublist)

sublist = mylist[::4] #jump every 3 times
print(sublist)

#max & min
print(max(mylist))
print(min(mylist))

#how to get the index of an element
index = mylist.index(3, 1)	#define the index from which you want to search
print(index)

#using list as stack
color_list=["Red", "Blue", "Green", "Black"]
color_list.pop() #LIFO
print(color_list)

#using list as queue
from collections import deque
color_list = deque(["red", "green", "blue", "yellow"])
color_list.popleft() 
print(list(color_list))

#extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
c = [*a,*b]
print(c)

#sort
a = [1,5,6,9,2,4]
a.sort()
print(a)

#count
print(a.count(2))

#shallow copy
import copy

a = [1,2,[3,4]]
b = a.copy()
print(b)
a[2][0]= 5
print(a)
print(b) # values changes w.r.t to a

#deepcopy
import copy
a = [2,3,4,[5,6]]
b = copy.deepcopy(a)
a[3][0] = 7
print(a)
print(b) # independent

##list comprehensive
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)  # Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

fruits = ['apple', 'banana', 'cherry', 'date']
short_fruits = [fruit.upper() for fruit in fruits if len(fruit) <= 5]
print(short_fruits) 

list3 = [1,2,1,4,5,6,6,7,7,8]

list4 = list(dict.fromkeys(list3))
print(list4)

'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''