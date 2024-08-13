def is_palindrome(str):
    if str == str[::-1]:
        print("Given string is palindrome")
        
    else:
        print("Not a palindrome")    
        
str = input("Enter the string: ")

print(is_palindrome(str))        