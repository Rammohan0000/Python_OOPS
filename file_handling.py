# file handling in python
# 1. File Streams
    # A file stream refers to flow of data between a file and a program. 
    # Python provides functions to open, read, write, and close files.
    # opening a file using open() function
    # modes like -> r(read), w(write), a(apend), b(binary mode) and + (read,write)
    # closing a file using file.close()
    # Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a file stream example!")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  

# 2. File Processing -> reading or writting files in various ways
   # reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Removes trailing newline

   # writting multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
with open('example.txt', 'w') as file:
    file.writelines(line + '\n' for line in lines)

  # appending to a file (end of the file)
with open('example.txt', 'a') as file:
    file.write("Appended line!\n")
  
# 3. Diagnosis file stream problems
    # FileNotFoundError
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

    # Permission Denied 
try:
    with open('/root/important.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("You don't have permission to access this file.")

# seek() -> moves a file pointer to a specific location
# tell() -> returns the current position of the file pointer
with open('example.txt', 'r') as file:
    print(file.tell())  # Output: 0 (start of the file)
    file.seek(5)
    print(file.read())  # Reads from the 5th character onward

# read only parts of the file
f = open("demofile.txt", "r")
print(f.read(5))

# Readlines -> to return one line
f = open("demofile.txt", "r")
print(f.readline())

# split lines 
with open("geeks.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

# delete a file
import os
os.remove("demofile.txt")

# check file exists or not
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


#  Python handles binary files using file modes like 'rb' (read binary) and 'wb'
# Writing binary data to a file
data = b"This is binary data.\nSecond line of binary data."
with open('binary_example.bin', 'wb') as file:
    file.write(data)

# Reading binary data from a file
with open('binary_example.bin', 'rb') as file:
    content = file.read()
    print(content)  
# copying binary files
with open('source_image.jpg', 'rb') as src_file:
    with open('destination_image.jpg', 'wb') as dest_file:
        dest_file.write(src_file.read())
print("Image copied successfully!")


