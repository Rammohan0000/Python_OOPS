# generator is a special type of iterator that allows you to iterate over a sequence of values lazily.
# Unlike lists, generators do not store all values in memory at once; instead, they generate values one at a time
# Values are computed only when needed, which can improve performance.
# Generators are defined using the def keyword and use the yield statement to produce values one at a time.
# The yield statement pauses the function, saving its state, and resumes from the same state when called again.
# for list we use sqaure brackets, whereas generators uses ()
# generator for a range
def custom_range(start, end):
    while start < end:
        yield start
        start += 1

for number in custom_range(1, 5):
    print(number)

# fibonacci Sequence using generators
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

#ssmple example
def my_generator():
    yield 1
    yield 2
    yield 3
gen = my_generator()
print(next(gen))
print(next(gen)) 
print(next(gen))

# counter using generator function
def count_to_max(max):
    count = 1
    while count<= max:
        yield count
        count += 1
counter = count_to_max(10)
for num in counter:
    print(num)       
