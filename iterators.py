# iterators -> allows you to traverse through a sequence of elements, one element at a time, without needing to load the entire sequence into memory.
#  an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#  Iterators compute the next value only when needed Object that can return an iterator using iter(). Examples: list, string.
# iterable vs iterator -> an iterable object that can return an iterator using iter(). Examples: list, string.
# iterator is Object with __iter__() and __next__() methods.
# __iter__() (Returns the iterator object itself.)
# __next__() Returns the next element in the sequence. Raises StopIteration when done.
# raises a StopIteration exception when there are no more items to return
# using iterator directly
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# creating custom iterator
class Squares:
    def __init__(self, max_num):
        self.num = 0
        self.max_num = max_num
    def __iter__(self):
        return self
    def __next__(self):
        if self.num >= self.max_num:
            raise StopIteration
        self.num += 1
        return self.num ** 2
squares = Squares(5)
for square in squares:
    print(square)

# iterators vs loops
my_list = [10, 20, 30]
#using for loop
for item in my_list:
    print(item)
# Equivalent iterator usage
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break

