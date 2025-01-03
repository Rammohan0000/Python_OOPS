# strings are sequence of characters and immutable
# string are stored in arrays of characters

words = ["python", "is", "fun"]
print(" ".join(words))

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
