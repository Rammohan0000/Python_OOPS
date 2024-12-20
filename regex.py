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
      # \a: returns a match if the specified character are at beginning of string

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
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#IPv4 address validation
ip_addr = input("Enter the IP-Address for the validation")
pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
if re.findall(pattern, ip_addr):
    print(f"given ip addr {ip_addr} is valid IP-Addr")
else:
    print("not a valid ip-address")    
