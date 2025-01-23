# strings are sequence of characters and immutable
# string are stored in arrays of characters

words = ["python", "is", "fun"]
print("$".join(words))

#char to ascii value
char = "a"
print(ord(char))
#ascii to char value
ascii_value = 65
char = chr(ascii_value)
print(f"The character for ASCII value {ascii_value} is '{char}'")  # Output: The character for ASCII value 65 is 'A'

class StringOperations:
    def __init__(self, input_string):
        self.input_string = input_string  # Encapsulating the string

    def to_uppercase(self):
        return self.input_string.upper()  # Convert to uppercase

    def to_lowercase(self):
        return self.input_string.lower()  # Convert to lowercase

    def is_alphanumeric(self):
        return self.input_string.isalnum()  # Check if alphanumeric

    def word_count(self, word):
        return self.input_string.count(word)  # Count occurrences of a word

    def reverse_string(self):
        return self.input_string[::-1]  # Reverse the string

    def replace_word(self, old_word, new_word):
        return self.input_string.replace(old_word, new_word)  # Replace words

    def split_string(self, delimiter=" "):
        return self.input_string.split(delimiter)  # Split the string

    def starts_with(self, prefix):
        return self.input_string.startswith(prefix)  # Check prefix

    def ends_with(self, suffix):
        return self.input_string.endswith(suffix)  # Check suffix

    def remove_whitespace(self):
        return self.input_string.strip()  # Remove leading and trailing whitespace

# Example usage
string_obj = StringOperations("   Hello World, welcome to Python!   ")

print("Original String:", string_obj.input_string)
print("Uppercase:", string_obj.to_uppercase())
print("Lowercase:", string_obj.to_lowercase())
print("Is Alphanumeric:", string_obj.is_alphanumeric())
print("Word Count ('World'):", string_obj.word_count("World"))
print("Reversed String:", string_obj.reverse_string())
print("Replace 'World' with 'Universe':", string_obj.replace_word("World", "Universe"))
print("Split by space:", string_obj.split_string())
print("Starts with 'Hello':", string_obj.starts_with("Hello"))
print("Ends with 'Python!':", string_obj.ends_with("Python!"))
print("Trimmed String:", string_obj.remove_whitespace())


'''
Method	           Description
capitalize()	   Converts the first character to upper case
casefold()	       Converts string into lower case
center()	       Returns a centered string
count()	           Returns the number of times a specified value occurs in a string
encode()	       Returns an encoded version of the string
endswith()	       Returns true if the string ends with the specified value
expandtabs()	   Sets the tab size of the string
find()	           Searches the string for a specified value and returns the position of where it was found
format()	       Formats specified values in a string
format_map()	   Formats specified values in a string
index()	           Searches the string for a specified value and returns the position of where it was found
isalnum()	       Returns True if all characters in the string are alphanumeric
isalpha()	       Returns True if all characters in the string are in the alphabet
isascii()	       Returns True if all characters in the string are ascii characters
isdecimal()	       Returns True if all characters in the string are decimals
isdigit()	       Returns True if all characters in the string are digits
isidentifier()	   Returns True if the string is an identifier
islower()	       Returns True if all characters in the string are lower case
isnumeric()	       Returns True if all characters in the string are numeric
isprintable()	   Returns True if all characters in the string are printable
isspace()	       Returns True if all characters in the string are whitespaces
istitle()	       Returns True if the string follows the rules of a title
isupper()	       Returns True if all characters in the string are upper case
join()	           Converts the elements of an iterable into a string
ljust()	           Returns a left justified version of the string
lower()	           Converts a string into lower case
lstrip()	       Returns a left trim version of the string
maketrans()	       Returns a translation table to be used in translations
partition()	       Returns a tuple where the string is parted into three parts
replace()	       Returns a string where a specified value is replaced with a specified value
rfind()	           Searches the string for a specified value and returns the last position of where it was found
rindex()	       Searches the string for a specified value and returns the last position of where it was found
rjust()	           Returns a right justified version of the string
rpartition()	   Returns a tuple where the string is parted into three parts
rsplit()	       Splits the string at the specified separator, and returns a list
rstrip()	       Returns a right trim version of the string
split()	           Splits the string at the specified separator, and returns a list
splitlines()	   Splits the string at line breaks and returns a list
startswith()	   Returns true if the string starts with the specified value
strip()	           Returns a trimmed version of the string
swapcase()	       Swaps cases, lower case becomes upper case and vice versa
title()	           Converts the first character of each word to upper case
translate()	       Returns a translated string
upper()	           Converts a string into upper case
zfill()	           Fills the string with a specified number of 0 values at the beginning
'''