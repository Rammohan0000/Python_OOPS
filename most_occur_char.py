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

# most occurring character
def most_occuring_char(occurance_dict):
    max_char = max(occurance_dict, key=occurance_dict.get)
    return max_char
occurance_dict = occurance(str)
print(f"The most occurring character is: {most_occuring_char(occurance_dict)}")

#longest word
def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    return longest_word
sentence = "Python programming is both fun and challenging"
longest = find_longest_word(sentence)
print(f"The longest word is: {longest}")

#shortest word  
def find_shortest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    shortest_word = min(words, key=len)  # Find the word with the minimum length
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

#swipe first and last character of a string
def swap_first_last_char(str):
    return str[-1] + str[1:-1] + str[0]
str = input("Enter a string: ")
print(swap_first_last_char(str))

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

#remove special characters from a string
def remove_special_char(str):
    result = ""
    for i in str:
        if i.isalnum():
            result = result + i
    return result
str = input("Enter a string: ")
print(remove_special_char(str))

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



