# regex -> used to search, match, or manipulate strings based on specific patterns.
# regex functions are re.match(), re.search(), re.findall() and re.finditer()
      # re.match() -> checks for a match at begining of a string
      # re.search() -> searches for the first match of pattern anywhere in the string
      # re.findall() -> returns all occurance of the pattern in the string as a list
      # re.finditer() -> returns an iterator yielding match objects for all matches in the string
      # re.sub() -> replaces occurances of the pattern with a specified string
      # re.split() -> splits the string based on the pattern 
# common regex syntax are -->
      # .: Matches any character except a newline.
      # ^: Matches the beginning of the string.
      # $: Matches the end of the string.
      # *: Matches 0 or more repetitions of the preceding character.
      # +: Matches 1 or more repetitions of the preceding character.
      # ?: Matches 0 or 1 repetition of the preceding character.
      # {m,n}: Matches between m and n repetitions of the preceding character.
      # [abc]: Matches any character inside the brackets.
      # [^abc]: Matches any character not inside the brackets.
      # \d: Matches any digit (0-9).
      # \D: Matches any non-digit.
      # \s: Matches any whitespace (space, tab, etc.).
      # \S: Matches any non-whitespace character.
      # \w: Matches any alphanumeric character or underscore.
      # \W: Matches any non-alphanumeric character.
      # \b: beginning or end of word
      # \B: Not at beginning or end of word
      # \a: returns a match if the specified character are at beginning of string.

# match a pattern at start of the string
import re
pattern = r'hello'
text = 'hi_world'
if re.match(pattern,text):
    print('true')
else: 
    print('pls check your regex condition')    

# search for the pattern anywhere in a string
import re
pattern = r'cricket'
text = 'among all sports cricket is best'
if re.search(pattern,text,re.IGNORECASE):
    print('true')
else:
    print('pls check regex condition')    

# find all occurances
import re
pattern = r'childrens'
text = 'there are 4 childrens and those 4 childrens are studying in 2nd class'
matches = re.findall(pattern,text)
print(f"occurances are {matches} with count of {len(matches)}")

# replace patterns
import re
text = 'i like to play football'
replacement = 'cricket'
pattern = r'football'
new_text = re.sub(pattern, replacement, text)
print(new_text)

# splitting a string
import re
text = 'apple, banana, grape, mango'
pattern = r'[:,]'
fruits = re.split(pattern,text.strip())
result = ':'.join(fruits)
#print(fruits)
print((result))

# Extracting numbers
text = 'team score is 230 and kl_rahul score is 88'
pattern = r'\d+'
number = re.findall(pattern, text)
print(number)

#example
import re
pattern = r'ca*bb+t?'
text = 'ct, caat, cbb, cat'
words = text.split(',')
print(words)
for t in words:
   if re.findall(pattern, t):
       print(f'given word {t} is true')
   else:
       print(f'the given word is {t} false')   

# find dates in a string
text = "Today's date is 2024-12-19 and yesterday was 2024-12-18."
pattern = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(pattern, text)
print(dates)

# without using regex
def extract_dates(text):
    words = text.split()  # Split text into words
    dates = []  
    for word in words:
        parts = word.split('-')  # Check if it contains '-'
        if len(parts) == 3 and all(part.isdigit() for part in parts):  # Ensure all parts are digits
            dates.append(word)  # Append valid date   
    return dates
text = "Today's date is 2024-12-19 and yesterday was 2024-12-18."
dates = extract_dates(text)
print(dates)

# using finditer()
import re
text = "apple, banana, grape, mango, pineapple"
pattern = r'a\w+'  
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Match: {match.group()} at position {match.start()}-{match.end()}")

# usecase for group()
pattern = r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})"
match = re.search(pattern, "19-12-2024")
if match:
    print(match.group("day"), match.group("month"), match.group("year"))

# email validation
email = "test.email@domain.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# example
txt = "the rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#IPv4 address validation
ip_addr = input("Enter the IP-Address for the validation")
pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
if re.findall(pattern, ip_addr):
    print(f"given ip addr {ip_addr} is valid IP-Addr")
else:
    print("not a valid ip-address")    

# Regular expression with a named capturing group
import re
pattern = r"(?P<digit>\d+)"
text = "123"
match = re.search(pattern, text)
# Access the captured value using the group name
if match:
    print(match.group("digit")) 

# Match 'a' repeated between 2 and 4 times
import re
pattern = r'a{2,4}'
text = 'a aa aaa aaaa aaaaa'
matches = re.findall(pattern, text)
print(matches)  

# Match any single character 'a', 'b', or 'c'
import re
pattern = r'[abc]'
text = 'apple banana cherry date'
matches = re.findall(pattern, text)
print(matches) 

# Match any character except 'a', 'b', or 'c'
import re
pattern = r'[^abc]'
text = 'apple banana cherry date'
matches = re.findall(pattern, text)
print(matches) 

#write a python program to validate a phone number
import re
phone_number = input("Enter the phone number for validation")
pattern = r'^\d{10}$'
if re.findall(pattern, phone_number):
    print(f"given phone number {phone_number} is valid")
else:
    print("not a valid phone number")

#write a python program to remove leading zeros in an ip address
import re
ip_addr = input("Enter the IP-Address for the validation")
pattern = r'^0*'
new_ip = re.sub(pattern, '', ip_addr)
print(new_ip)

#write a python program to validate a password
import re
password = input("Enter the password for validation")
pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")

#validate phone number
import re
phone_number = input("Enter the phone number for validation")
pattern = r'^\d{10}$'
if re.findall(pattern, phone_number):
    print(f"given phone number {phone_number} is valid")
else:
    print("not a valid phone number")
    
###important program to extract interface details and convert them into a list of dictionaries
import re

def status(interface_data):
    # Updated regex to capture interface, IP, and state
    pattern = r"(?P<interface>\S+)\s+(?P<ip>\S+)\s+(?P<state>\S+)"
    matches = re.finditer(pattern, interface_data)
    details = [match.groupdict() for match in matches if match.group('state') == 'up']  # Collect all details as dictionaries
    return details

interface_data = '''
gigabitethernet0/1  192.168.1.1   up
gigabitethernet0/2  192.168.1.2   down
gigabitethernet0/3  192.168.1.3   down
gigabitethernet0/4  192.168.1.4   down
'''

details = status(interface_data)

# Print all interface details
for detail in details:
    print(f"Interface: {detail['interface']}, IP: {detail['ip']}, State: {detail['state']}")

# Accessing details list
for idx, detail in enumerate(details):
    print(f"Details for Interface {idx + 1}: {detail}")

# Attempt to use dictionary-specific methods on the list will raise an error
# To access keys/values for individual dictionaries in the list:
for detail in details:
    print(f"Keys: {detail.keys()}")
    print(f"Values: {detail.values()}")
    print(f"Items: {detail.items()}")

# extract words which are ending with vowels
import re
def vowels(inputs):
    pattern = re.compile(r'[aeiou]$')
    matches = [word for word in inputs if pattern.search(word)]
    return matches
inputs = ['cat', 'dog', 'free', 'tree']
print(vowels(inputs))

# extract words which are starting with vowels
import re
inputs = ['ct', 'dog', 'apple', 'orange']
out_vowels = []
out_conso = []
pattern = re.compile(r'[aeiouAEIOU]')  # Pattern to check if a word contains at least one vowel

for word in inputs:
    if pattern.search(word):  # If a vowel is found in the word
        out_vowels.append(word)
    else:
        out_conso.append(word)

print("Words with vowels:", out_vowels)
print("Words with only consonants:", out_conso)

