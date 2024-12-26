class MaxMin:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_max(self):
        return max(self.numbers)

    def get_min(self):
        return min(self.numbers)

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_min = MaxMin(numbers)
print("Max:", max_min.get_max())
print("Min:", max_min.get_min())

# 2nd example usage:
lst = list(map(int, input("Enter the list of numbers: ").split()))
max_val, min_val = lst[0], lst[0]
for x in lst:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x
print("Max:", max_val)
print("Min:", min_val)

# 2nd largest element in a list
def second_largest(lst):
    unique_list = list(set(lst))
    if len(unique_list) < 2:
        return None
    unique_list.sort(reverse=True)
    return unique_list[1]
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("2nd largest:", second_largest(lst))

# count vowels in a string
def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count
s = input("Enter a string: ")       
print("Vowels count:", count_vowels(s))

# swap first and last element
def swap_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("After swapping:", swap_first_last(lst))

# reverse a list
def reverse_list(lst):
    return lst[::-1]
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("Reversed list:", reverse_list(lst))

# check if a word is palindrome
def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a word: ")
print("Palindrome:", is_palindrome(s))

# check if word is anaagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
s1 = input("Enter the 1st word: ")
s2 = input("Enter the 2nd word: ")
print("Anagram:", is_anagram(s1, s2))

# find a word which is greater than given length
def find_long_words(lst, n):
    return [word for word in lst if len(word) > n]
lst = input("Enter the list of words: ").split()
n = int(input("Enter the length: "))
print("Words greater than length", n, "are:", find_long_words(lst, n))

#Count the occurrences of each word in a given sentence
def word_count(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# to print specified list after removing 0th, 4th and 5th elements
def remove_elements(lst):
    return [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("After removing 0th, 4th and 5th elements:", remove_elements(lst))

# to check common in two lists
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
lst1 = list(map(int, input("Enter the 1st list of numbers: ").split()))
lst2 = list(map(int, input("Enter the 2nd list of numbers: ").split()))
print("Common elements:", common_elements(lst1, lst2))

# to find the difference between two lists
def difference_elements(lst1, lst2):
    return list(set(lst1) - set(lst2))
lst1 = list(map(int, input("Enter the 1st list of numbers: ").split()))
lst2 = list(map(int, input("Enter the 2nd list of numbers: ").split()))
print("Difference elements:", difference_elements(lst1, lst2))

# to find the union of two lists
def union_elements(lst1, lst2):
    return list(set(lst1) | set(lst2))
lst1 = list(map(int, input("Enter the 1st list of numbers: ").split()))
lst2 = list(map(int, input("Enter the 2nd list of numbers: ").split()))
print("Union elements:", union_elements(lst1, lst2))

#flatten a shallow list
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
lst = [[1, 2, 3], [4, 5], [6, 7, 8]]
print("Flattened list:", flatten_list(lst))

# to find the common elements in nested lists
def common_elements_nested(lst):
    return list(set.intersection(*map(set, lst)))
lst = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print("Common elements in nested lists:", common_elements_nested(lst))

#count frequency of elements in a list
def frequency_elements(lst):
    return {x: lst.count(x) for x in lst}
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("Frequency of elements:", frequency_elements(lst))
#2nd method
import collections
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("Frequency of elements:", collections.Counter(lst))

#example for args, kwargs
# args -> tuple of positional arguments passed to a function call 

def add(*args):
    return sum(args)
def add(*args):
    return sum(args)
print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#kwargs -> dictionary of keyword arguments passed to a function call
def add(**kwargs):
    return sum(kwargs.values())
print(add(a=1, b=2, c=3))
print(add(a=1, b=2, c=3, d=4, e=5))

#args and kwargs together
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
print(add(1, 2, 3, a=4, b=5, c=6))

# to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print("Factorial:", factorial(n))