# Write a Python function that takes a list of numbers and returns True if the list contains 2 occurrences of 19 and 3 occurrences of 5, otherwise it returns False.
def occurances(lst):
    target1 = 19
    target2 = 5
    count1 = lst.count(target1) # count 19 3 times
    count2 = lst.count(target2) # count 5 2 times
    return count1 == 2 and count2 == 3

lst = list(map(int,input("enter the nos: ").split(' ')))
print(occurances(lst))

# len(lst) == 8 checks if the list has 8 elements and fifth element is repeated 3 times
def occurances(lst):
    return len(lst) == 8 and lst.count(lst[4]) == 3
lst = list(map(int,input("enter the nos: ").split(' ')))
print(occurances(lst))
        
# write a python program that takes integers between 0 to 999 and return true if which all differ by 10 from one another
def differ_by_10(lst):
    for i in range(len(lst)-1):
        if abs(lst[i] - lst[i+1]) != 10:
            return False
    return True
lst = list(range(0,1000,10))
print(differ_by_10(lst))

# write a python program that takes a list of integers and returns True if the list contains 3 even numbers in a row, otherwise it returns False.
def even_numbers(lst):
    for i in range(len(lst)-2):
        if lst[i] % 2 == 0 and lst[i+1] % 2 == 0 and lst[i+2] % 2 == 0:
            return True
    return False
lst = list(map(int,input("enter the nos: ").split(' ')))
print(even_numbers(lst))

# write a python program that takes a list of integers and returns True if the list contains 3 increasing numbers in a row, otherwise it returns False.
def increasing_numbers(lst):
    for i in range(len(lst)-2):
        if lst[i] < lst[i+1] and lst[i+1] < lst[i+2]:
            return True
    return False
lst = list(map(int,input("enter the nos: ").split(' ')))
print(increasing_numbers(lst))

# write a python program to check sum of first of i elements is equal i
def sum_of_i_elements(lst):
    for i in range(1,len(lst)):
        if sum(lst[:i]) == i:
            return True
    return False
lst = list(map(int,input("enter the nos: ").split(' ')))
print(sum_of_i_elements(lst))

# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
def split_string(s):
    words = s.split(', ')
    separators = [', ' for i in range(len(words)-1)]
    return words, separators
s = input("enter the string: ")
print(split_string(s))


# write a python program that contains exactly 4 distinct values across the list such that no value is repeated more than once consecutively among the first 20 numbers
def test(nums):
    return all([nums[i] != nums[i+1] for i in range(20)]) and len(set(nums)) == 4
nums = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1]
print(test(nums))

# write a python program to split it into groups of perfectly matched parantheses without any whitespace
def split_groups(s):
    return [i for i in s.split('()') if i != '']
s = input("enter the string: ")
print(split_groups(s))

# check palindrome in a list
def palindrome(strs):
    return [s == s[::-1] for s in strs]
strs = input("enter the string: ")
print(palindrome(lst))

# find strings in a given list starting with a given prefix
def find_strings(strs,prefix):
    return [s for s in strs if s.startswith(prefix)]
strs = input("enter the string: ").split(' ')
prefix = input("enter the prefix: ")
print(find_strings(lst,prefix))

# length of strings in list
def length_of_strings(strs):
    return [len(s) for s in strs]
strs = input("enter the string: ").split(' ')
print(length_of_strings(strs))

# sum of ASCII values of uppercase letters
def sum_of_ascii_values(s):
    return sum([ord(c) for c in s if c.isupper()])
s = input("enter the string: ")
print(sum_of_ascii_values(s))

# string with most unique characters
def most_unique_characters(strs):
    return max(strs, key = lambda s: len(set(s)))
strs = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
print(most_unique_characters(strs))

# write a python program to return two digit numbers only from a list
def two_digit_numbers(nums):
    return [n for n in nums if 9 < n < 100]
nums = list(map(int,input("enter the nos: ").split(' ')))
print(two_digit_numbers(nums))

# Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.
def sum_of_numbers(nums,k):
    return sum([n for n in nums[:k] if n > 9])
nums = list(map(int,input("enter the nos: ").split(' ')))
k = int(input("enter the k value: "))
print(sum_of_numbers(nums,k))

# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
def product_of_odd_digits(number):
    number = abs(number)  # Ensure the number is positive
    product = 1
    has_odd = False

    for digit in str(number):
        digit = int(digit)
        if digit % 2 != 0:  # Check if the digit is odd
            product *= digit
            has_odd = True
    return product if has_odd else 0
print(product_of_odd_digits(123456789))  # Output: 945
print(product_of_odd_digits(2468))       # Output: 0
print(product_of_odd_digits(13579))      # Output: 945
print(product_of_odd_digits(-531))       # Output: 15

# find all words in a given string with n consonants
def words_with_n_consonants(s,n):
    return [word for word in s.split() if sum(1 for c in word if c.lower() not in 'aeiou') == n]
s = input("enter the string: ")
n = int(input("enter the n value: "))
print(words_with_n_consonants(s,n))

# Write a Python program to find the sum of the numbers in a given list of strings, considering the numbers in the strings.
def sum_of_numbers(strs):
    return sum([int(s) for s in strs if s.isdigit()])
strs = input("enter the string: ").split(' ')
print(sum_of_numbers(strs))

# find even palindrome in a list
def even_palindrome(lst):
    return [s for s in lst if len(s) % 2 == 0 and s == s[::-1]]
lst = input("enter the string: ").split(' ')
print(even_palindrome(lst))

# Write a Python program to find the indices of two entries that show that the list is not in increasing order. If there are no violations (they are increasing), return an empty list.
def find_violations(lst):
    return [i for i in range(len(lst)-1) if lst[i] > lst[i+1]]
lst = list(map(int,input("enter the nos: ").split(' ')))
print(find_violations(lst))

# sort by digit sum
def sort_by_digit_sum(lst):
    return sorted(lst, key = lambda x: sum(int(d) for d in str(x))) 
lst = list(map(int,input("enter the nos: ").split(' ')))
print(sort_by_digit_sum(lst))

# find even palindrome in a list
def even_palindrome(lst):
    return [s for s in lst if len(s) % 2 == 0 and s == s[::-1]]
lst = input("enter the string: ").split(' ')
print(even_palindrome(lst))

# sort even length words
def sort_even_length_words(lst):
    return sorted([word for word in lst if len(word) % 2 == 0])
lst = input("enter the string: ").split(' ')
print(sort_even_length_words(lst))

# Write a Python program to reverse the case of all strings. For those strings, which contain no letters, reverse the strings.
def reverse_case(lst):
    return [s.swapcase() if any(c.isalpha() for c in s) else s[::-1] for s in lst]
lst = input("enter the string: ").split(' ')
print(reverse_case(lst))

# sum of even elements at odd indices
def even_count(lst):
    return sum(i for i in lst if i %2==0)
lst = list(map(int, input("Enter the nos: ").split()))
print(even_count(lst))

# converting lower case to upper case
def test(strs: list[str]) -> list[str]:
    return [s.upper() for s in strs]
result = test(['hello', 'world'])
print(result)

