def remove_and_print_every_third(numbers):
    index = 0
    while len(numbers) > 0:
        index = (index + 2) % len(numbers)  # Move to every third element
        print(numbers.pop(index))  # Remove and print the element

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_and_print_every_third(numbers)
