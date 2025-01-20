# set is A mutable collection of unique, unordered elements.
# Unordered: No indexing or slicing; the elements' order is not guaranteed.

# Creating a set
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Adding an element
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

# Checking membership
print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set_a & set_b)  # Output: {3}

# Difference
print(set_a - set_b)  # Output: {1, 2}


## frozenset is an immutable set that can be used as a dictionary key.
# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})

# Checking membership
print(3 in my_frozenset)  # Output: True
print(5 in my_frozenset)  # Output: False

# Set operations
fs_a = frozenset([1, 2, 3])
fs_b = frozenset([3, 4, 5])

# Union
print(fs_a | fs_b)  # Output: frozenset({1, 2, 3, 4, 5})

# Intersection
print(fs_a & fs_b)  # Output: frozenset({3})

# Difference
print(fs_a - fs_b)  # Output: frozenset({1, 2})

# Attempting to modify (will raise an error)
# my_frozenset.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'
