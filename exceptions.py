# error stops flow of execution
# types of erros
# syntax error -> syntax of language not followed # indentation error
# logical error -> incorrect results -> incorrect behaviour

# how to overcome logical errors -> exception handling
# Exceptions occur during the execution of the program and can be handled using try, except and finally blocks.
# common types of exceptions
# 1.Zero division errors -> occurs when trying to divide a number by zero
x = 1
y = 0
try:
    print(x /y)
except ZeroDivisionError:
    print("you cant divide by zero")

#2.Value Error -> inappropriate value
try:
    number = int('hello')
except ValueError:
    print("Invalid value! cannot convert to integer. ")

#3. Type Error -> inappropriate type
try:
    result = 'hello' + 10
except TypeError:
    print("type mismatch! cannot add string to an integer")

#4. Index Error -> invalid index is accessed in a list
list = [1,2,3]
try:
    print(list[5])
except IndexError:
    print("Index out of range! ")        

#5. KeyError -> key doesnt exist in a dictionary
dict = {'name':'john', 'age': 25} 
try:
    print(dict['country'])
except KeyError:
    print("key not found in the dictionary") 

#6.FileNotFoundError -> file doesnt exist
try:
    with open("file.txt",'r') as file:
        content = file.read()
except FileNotFoundError:
    print("file not found")                     

#7. Attribute Error -> accessing attribute or method that doesnt exist on an object
str ="hello"
try:
    str.append("world")
except AttributeError:
    print("string object has no method append")    

# Multiple Exception Handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

#Else and Finally Blocks
#Else block: Executes if no exception is raised
#finally block: Always runs, with regardless of exceptions raised
try:
    x = 10 / 2  # No exception
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("This will always execute.")

