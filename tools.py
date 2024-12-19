# lambda functions -> it is an nameless function, defined using lambda keyword
# they are typically used for small, single-use functgions
# syntax: -> lambda arguments: expression
# Traditional function
def add(x, y):
    return x + y
# Lambda equivalent
add_lambda = lambda x, y: x + y
print(add(3, 5))        
print(add_lambda(3, 5)) 

# Sort list of tuples by the second value
data = [(1, 'B'), (2, 'A'), (3, 'C')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data) 

#  map function -> it applies a given function to all items in an iterable(like list or tuple)
# syntax: -> map(function,iterable)\
numbers = [1, 2, 3, 4, 5]
# Using lambda with map
squares = list(map(lambda x: x**2, numbers))
print(squares)  

#convert str to integer
str_numbers = ["1", "2", "3"]
int_numbers = list(map(int, str_numbers))
print(int_numbers) 

# Filter function -> filters elements of an iterable based on a condition provided by a function
# syntax -> filter(function,iterable)
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

words = ["apple", "banana", "pear", "cherry"]
filtered_words = list(filter(lambda word: len(word) > 5, words))
print(filtered_words)

# combined use of lambda, map and filter
numbers = [1, 2, 3, 4, 5, 6]
# Filter even numbers and find their squares
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

words = ["python", "is", "fun", "to", "learn"]

# Filter words with length > 2 and capitalize them
result = list(map(lambda word: word.upper(), filter(lambda word: len(word) > 2, words)))
print(result) 


