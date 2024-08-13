def length_of_last_word(s: str) -> int:
    # Strip any trailing spaces and split the string into words
    words = s.strip().split()
    
    # Return the length of the last word
    if words:
        return len(words[-1])
    else:
        return 0

# Example usage:
input_string = "Hello World"
print(f"Length of the last word: {length_of_last_word(input_string)}")
