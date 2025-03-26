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
        
#armstrong number
def is_armstrong(number):
    num_str = str(number)  # Convert number to string
    num_digits = len(num_str)  # Count number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)  # Compute Armstrong sum
    return armstrong_sum == number  # Check if Armstrong sum matches original number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is NOT an Armstrong number.")
      
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

#find substring in a string
def find_substring(s,sub):
    return s.find(sub)
s = input("enter the string: ")
sub = input("enter the substring: ")
print(find_substring(s,sub))

#without using find
def find_substring(s,sub):
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
s = input("enter the string: ") 
sub = input("enter the substring: ")
print(find_substring(s,sub))


# find abc in a string
import re
text = 'abcxyzsdghiueabcxyzadjnsadkjhefaoiuahaaabaabaabababaxyxyxyxasdaaaaabcabcxyzxyz'
matches = list(re.finditer('abc', text))
for match in matches:
    print(f"Found 'abc' at: {match.start()}")
for idx, char in enumerate(text):
    if char == 'a':
        print(f"The index of 'a' is: {idx}")

# find the first non-repeating character in a string
def first_non_repeating_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
s = input("enter the string: ")
print(first_non_repeating_char(s))

# find second most repeated character in a string
def second_most_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_count[1][0]
s = input("enter the string: ")
print(second_most_repeated_char(s))

# find second largest word in  a string
def second_largest_word(s):
    words = s.split()
    words.sort(key=len)
    return words[-2]
s = input("enter the string: ")
print(second_largest_word(s))

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

# find words with vowels and consonants
inputs = ['sky', 'apple', 'tree', 'rhythm', 'free', 'cat', 'gym']
out_vowels = []
out_conso = []
vowels = 'aeiouAEIOU'
for word in inputs:
    if any(char in vowels for char in word):  
        out_vowels.append(word)
    else:
        out_conso.append(word)
print("Words with vowels:", out_vowels)
print("Words with only consonants:", out_conso)

#2nd highest number
l = [1,7,3,2,7,2]

freq_dict = {}

for num in l:
    freq_dict[num] = freq_dict.get(num,0) + 1 
print(freq_dict)  
most_freq, max_count = None,0
if freq_dict[num] > max_count:
    most_freq, max_count = num , freq_dict[num] 
    print(most_freq, max_count)
x = sorted(freq_dict.items(), key = lambda x: x[1], reverse = 'True')
print(x[1][0])

# find the sum of two numbers equal to target
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j] # for indices
                return [nums[i],nums[j]] # for values
    return None
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))





