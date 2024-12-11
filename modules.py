# Module is file containing Python code (functions, classes, and variables) that can be imported and reused in other Python scripts or modules
#Encourages code reusability
#Provides built-in functionality with standard modules (e.g., math, os, random).

#save it with example_module.py
def add(a,b):
    return a + b

person1 = {
    "name":'john',
    "age": 25,
    "country":'USA'
}

#create a new python file, import the above python code using
#import example_module
#print(add(1,2))
#we can access variables also
#a = example_module.person1['age']
#print(a)

#renaming an module by using alias
#import example_module as em
#a = em.person1["name"]
#print(a)

#using *-> importing entire module
from math import *
print("Square root of 16:", sqrt(16))
print("Factorial of 5:", factorial(5))
print("GCD of 48 and 18:", gcd(48, 18))
print("LCM of 4 and 5:", lcm(4, 5))
print("2 raised to the power of 3:",pow(2, 3))
print("Ceiling of 4.3:", ceil(4.3))
print("Floor of 4.7:", floor(4.7))

#random module->used to generate random numbers and perform random operations on sequences
import random
print("random float between 0 and 1: ", random.random())
print("random integer between 1 and 10: ", random.randint(1,10))
print("random number in range 0 to 100 (step of 10):", random.randrange(0, 100, 10))
#random choice from sequence
cities = ['vizag', 'hyd','bng','chennai','kochi']
print("I want to visit: ", random.choice(cities))
#shuffle a sequence
cards = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(cards)
print("Shuffled cards:", cards)
#simulating a rolling dice
def roll_dice():
    return random.randint(1,6)
print("Dice roll result:", roll_dice())
#Example: Lottery Number Generator
def lottery_numbers():
    # Generate 6 unique random numbers between 1 and 49
    return sorted(random.sample(range(1, 50), 6))
print("Lottery numbers:", lottery_numbers())
#random password generator
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))
print("Random password:", generate_password(12))

#platform module->access information about the underlying platform, such as the operating system, hardware, and Python version.
# It is useful for debugging, compatibility checks, or logging system details.
import platform
print("System Name:", platform.system())
print("Node Name:", platform.node())
print("OS Release:", platform.release())
print("OS Version:", platform.version())
print("Processor:", platform.processor())
print("Platform Information:", platform.platform())
#using uname()
info = platform.uname()
print("System:", info.system)
print("Node Name:", info.node)
print("Release:", info.release)
print("Version:", info.version)
print("Machine:", info.machine)
print("Processor:", info.processor)
#checking compatibility
if platform.system() == "Windows":
    print("You are running on Windows!")
else:
    print("Not running on Windows.")

# os module -> provides functions for interacting with the operating system
# It allows you to perform tasks like file and directory management, process handling, environment variable access, and more.
import os
cwd = os.getcwd()
print("Current Working Directory is: ", cwd)
#list files in a directory
files = os.listdir(".") #"." refers to the current directory
print("Files:",files)
#change current directory
#os.chdir("/path/to/directory")
#print("changed directory:",os.getcwd())
#create a new directory
os.mkdir("demo")
print("directory created!")
#removing directory
os.rmdir("demo")
print("directory removed")
#creating nested directory
os.makedirs("parent_folder/child_folder")
print("nested directory created")
#removing nested directory
os.removedirs("parent_folder/child_folder")
print("nested directory removed")
#renaming a file or directory
#os.rename("requirement.txt","requirements.txt")
#print("File Renamed!")
#check of path exists or not
print(os.path.exists("lists.py"))
#get file size
size = os.path.getsize("dictionary.py")
print("File Size: ", size, "bytes")
#open a file or program
os.startfile("pyats.py")
#process management
#1.Get Current Process ID
pid = os.getpid()
print("current process id is: ", pid)
#get username of current process
import getpass
username = getpass.getuser()
print("Username", username)
#search for files with a specific extension
directory = "."
for file in os.listdir(directory):
    if file.endswith('.py'):
        print("text file:", file)

#datetime module -> handling date and time-related operations.
#from datetime import datetime, date, time, timedelta
from datetime import *
now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)
#custom format
formatted_date = now.strftime("%m-%Y-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_date)
now = datetime.now()
#date arithmetic with timedelta
future_date = now + timedelta(days=10)
past_date = now - timedelta(days=10)
print("Future Date:", future_date)
print("Past Date:", past_date)

#calender module
import calendar
print(calendar.month(2024,12))
print(calendar.calendar(2024))
#find next leap year
current_year = 2024
while not calendar.isleap(current_year):
    current_year += 1
print("Next Leap Year:", current_year)
#get all fridays of a month
year = 2024
month = 12
fridays = [day for week in calendar.monthcalendar(year, month) for day in week if week[calendar.FRIDAY] != 0]
print("Fridays in December 2024:", fridays)

