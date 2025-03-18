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

#wipro 2nd question
sentence = '''Peter Piper picked a peck of pickled peppers
A peck of pickled peppers Peter Piper picked
If Peter Piper picked a peck of pickled peppers'''
words = sentence.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("Word count:", word_counts)
#unique values
unique_words = set(words)
print("Unique words:", unique_words)

#first and second higheest calculation
def highest_paid(employees_data):
    most = max(employees_data, key=employees_data.get)
    sorted_dict = sorted(employees_data.items(), key = lambda x:x[1],reverse=True)
    return  most,sorted_dict[1][0]
employees_data = {
    "Alice": 60000,
    "Bob": 75000,
    "Charlie": 50000,
    "David": 90000
}
s=highest_paid(employees_data)
print(f"the first highest_paid employee was {s[0]} and second highest paid employee was {s[1]}")

# find first non repeated value in a list
mylist = [2, 5, 6, 7, 8, 9, 10, 5, 2, 6]
for num in mylist:
    if mylist.count(num) == 1:
        print(num)
        break

#count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# replace vowels in a string
def replace_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in s:
        if char in vowels:
            result +='$'
        else:
            result += char
    return result
s = input("Enter a string: ")
print("String after replacing vowels:", replace_vowels(s))

#camel to snake
def camel_to_snake(s):
    result = [s[0].lower()]
    for char in s[1:]:
        if char.isupper():
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)
input_string = 'PythonExercises'
output_string = camel_to_snake(input_string)
print(output_string)

#replace_with$
word = 'Python_Exercises_are_difficult'
parts = word.split('_')
result = '$'.join(parts)
print(result)

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

def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    char_count1 = {}
    char_count2 = {}
    for char in s1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in s2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2
s1 = input("Enter the 1st word: ")
s2 = input("Enter the 2nd word: ")
print("Anagram:", is_anagram(s1, s2))

# find a word which is greater than given length
def find_long_words(lst, n):
    return [word for word in lst if len(word) > n]
lst = input("Enter the list of words: ").split()
n = int(input("Enter the length: "))
print("Words greater than length", n, "are:", find_long_words(lst, n))

# count the occurrences of each word in a given sentence
def word_count(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
sentence = input("Enter a sentence: ")
print("Word count:", word_count(sentence))

#converting string into dictionary
def string_to_dict(s):
    return dict(item.split(':') for item in s.split(','))
s = input("Enter a string: ")
print("Dictionary:", string_to_dict(s))

#2nd method
s = "name:Alice,age:25"
pairs = s.split(",")
d = {}
for pair in pairs:
    key, value = pair.split(":")
    d[key] = value
print(d)

# to find the length of the last word in a string
def length_last_word(s):
    words = s.split()
    if words:
        return len(words[-1])
    return 0
s = input("Enter a string: ")
print("Length of the last word:", length_last_word(s))

#count particular word in a sentence
def count_word_occurrences(sentence, word):
    words = sentence.split()
    count = words.count(word)
    return count
sentence = "I love reading books, I love playing cricket and I love watching movies."
word = "love"
occurrences = count_word_occurrences(sentence.lower(), word.lower()) 
print(f"The word '{word}' occurs {occurrences} times in the sentence.")

#most occured word in a sentence
def most_occured_word(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return max(word_counts, key=word_counts.get)
sentence = input("Enter a sentence: ")
print("Most occured word:", most_occured_word(sentence))

# to print specified list after removing 0th, 4th and 5th elements
def remove_elements(lst):
    return [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("After removing 0th, 4th and 5th elements:", remove_elements(lst))

#emunerate example
text = "hello"
for index, char in enumerate(text):
    print(f"Character at index {index}: {char}")

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"Index {index}: {fruit}")

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

#most freq element in a list
def most_frequent_element(lst):
    frequency = {x: lst.count(x) for x in lst}
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]
lst = list(map(int, input("Enter the list of numbers: ").split()))
most_frequent, count = most_frequent_element(lst)
print(f"The most frequent element is {most_frequent} with a frequency of {count}.")

#2nd method
import collections
lst = list(map(int, input("Enter the list of numbers: ").split()))
print("Frequency of elements:", collections.Counter(lst))

import collections
s = input("Enter a string: ")
print("Frequency of characters:", collections.Counter(s))

#example for args, kwargs
# args -> tuple of positional arguments passed to a function call 
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


