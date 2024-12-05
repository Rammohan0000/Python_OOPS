#tuple is ordered and unchangeable and allows duplicates
#methods cannot be used like insert,remove,pop,sort and reverse

#tuple constructor
mytuple = tuple(("a","b","c"))
print(mytuple)

#index
print(mytuple.index('c'))
#count
print(mytuple.count('a'))
#slicing
print(list(mytuple[1:2:1]))
#delete tuple
del mytuple
print(mytuple)
