#count occurance of each character
def occurance(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
str = input("Enter a string: ")
print(occurance(str))

# list with unique elements with first element
def occurrence(lst):
    freq_dict = {}
    for item in lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    unique_keys = [key for key, value in freq_dict.items() if value == 1]   
    return unique_keys[0]
mylist = [2, 5, 6, 7, 8, 9, 10, 5, 2, 6]
print(occurrence(mylist))

# most occurring character                                                 
def new(s):
    most = max(s, key = s.count)
    return most, s.count(most)
s = input("Enter the String: ")
result = new(s)
print(f"the most occured character is '{result[0]}' with frequency of {result[1]} ")

#without max function
def new(s):
    freq_dict = {}
    most_freq, max_count = None, 0
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
        if freq_dict[char] > max_count:
            most_freq,max_count = char, freq_dict[char]
    return most_freq, max_count
s = input("Enter the String: ")
result = new(s)
print(f"the most occured character is '{result[0]}' with frequency of {result[1]} ")

#longest word
def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = max(words, key=len) 
    return longest_word
sentence = "Python programming is both fun and challenging"
longest = find_longest_word(sentence)
print(f"The longest word is: {longest}")

#without using in-build functions
def find_longest_word(sentence):
    words = sentence.split()  
    longest_word = "" 
    for word in words:  
        if len(word) > len(longest_word):  
            longest_word = word  
    return longest_word
sentence = "Python programming is both fun and challenging"
longest = find_longest_word(sentence)
print(f"The longest word is: {longest}")

#shortest word  
def find_shortest_word(sentence):
    words = sentence.split()  
    shortest_word = min(words, key=len)  
    return shortest_word
sentence = "Python programming is both fun and challenging" 
shortest = find_shortest_word(sentence)
print(f"The shortest word is: {shortest}")

#count the number of words
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    return len(words)
sentence = "Python programming is both fun and challenging" 
print(f"The number of words in the sentence is: {count_words(sentence)}")

#without len function
def count_words(sentence):
    words = sentence.split()  # Split the sentence into words
    count = 0  # Initialize counter
    for _ in words:  # Iterate over words
        count += 1   # Increment counter
    return count
sentence = "Python programming is both fun and challenging"
print(f"The number of words in the sentence is: {count_words(sentence)}")

#swipe first and last character of a string
def swap_first_last_char(str):
    return str[-1] + str[1:-1] + str[0]
str = input("Enter a string: ")
print(swap_first_last_char(str))

# reverse a list without using in-build fucnctions
l = [1,2,3,4,5,6,7,8]
l2 = []
for i in range(len(l)-1, -1, -1):
    l2.append(l[i])
print(l2)    

# move 0's at the right end
l = [1,0,2,0,3,0,4,0,5,6,7]
result = [x for x in l if x!=0] + [0] * l.count(0)
print(result)

#remove nth index character from a string
def remove_char(str, n):
    first_part = str[:n] 
    last_part = str[n+1:]
    return first_part + last_part
str = input("Enter a string: ")
n = int(input("Enter the index of the character to remove: "))
print(remove_char(str, n))

#remove odd index characters from a string
def remove_odd_index_char(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
str = input("Enter a string: ")
print(remove_odd_index_char(str))

#odd index characters
def odd_index(str):
    if len(str) == 0:
        raise ValueError
    result = ''
    for i in range(len(str)):
        if i % 2 != 0:
            result +=str[i] 
    return result
str = 'rammohan'
print(odd_index(str))

#remove special characters from a string
def remove_special_char(str):
    result = ""
    for i in str:
        if i.isalnum():
            result = result + i
    return result
str = input("Enter a string: ")
print(remove_special_char(str))

#2nd method
def remove_special_char(s):
    return ''.join([char for char in s if char.isalnum()])
s = input("Enter a string: ")
print(remove_special_char(s))

#remove all characters except alphabets
def remove_special_char(str):
    result = ""
    for i in str:
        if i.isalpha():
            result = result + i
    return result
str = input("Enter a string: ")
print(remove_special_char(str))

#remove all characters except digits
def remove_special_char(str):
    result = ""
    for i in str:
        if i.isdigit():
            result = result + i
    return result
str = input("Enter a string: ")
print(remove_special_char(str))

#remove all characters except digits and alphabets  
def remove_special_char(str):
    result = ""
    for i in str:
        if i.isalnum():
            result = result + i
    return result
str = input("Enter a string: ")
print(remove_special_char(str))

#Convert a string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters
def convert_uppercase(str):
    counter = 0
    for i in str[:4]:
        if i.isupper():
            counter += 1
    if counter >= 2:
        return str.upper()
    return str
str = input("Enter a string: ")
print(convert_uppercase(str))

# write a python code to remove odd index characters from a string
def remove_odd_index_char(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result
str = input("Enter a string: ")
print(remove_odd_index_char(str))

# ASCII value of a character
a = 'I'
print(ord(a))

# ASCII value to character
a = 65
print(chr(a))

# find sum of two numbers equal to target
def two_numbers(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]
    return "No such numbers found"
nums = [10,20,10,40,50,60,70]
target = 50
print(two_numbers(nums, target))

# sorting a list of tupeles based on the second element
def sort_list(tuples):
    return sorted(tuples, key = lambda x: x[1]) 
tuples = [(1, 2), (3, 4), (1, 1), (5, 6), (7, 8), (1, 3)]
print(sort_list(tuples))

# sorting without using in-build functions
def sort_list(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i] , nums[j] = nums[j], nums[i]
    return nums
nums = [10, 20, 5, 6, 7, 8, 9]
print(sort_list(nums))

# sorting a string in alphabetical order
def sort_string(str):
    return ''.join(sorted(str))     
str = input("Enter a string: ")
print(sort_string(str))

# sorting a string without using in-build functions
def sort_string(str):
    str = list(str)
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] > str[j]:
                str[i], str[j] = str[j], str[i]
    return ''.join(str)
str = input("Enter a string: ")
print(sort_string(str))

# sorting a string in reverse order
def sort_string(str):
    return ''.join(sorted(str, reverse = True)) 
str = input("Enter a string: ")
print(sort_string(str)) 

# find the sum of three numbers equal to target
def three_numbers(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return nums[i], nums[j], nums[k]
    return "No such numbers found"
nums = [10,20,10,40,50,60,70]
target = 70
print(three_numbers(nums, target))
