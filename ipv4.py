import re

def ipv4_validation(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.findall(pattern,ip):
        parts = ip.split(".")
        for part in parts:
            if not part.isdigit or not 0<=int(part)<=255:
                return "Please Check your IP-Address"
        return True
    return "Please check your IP-Address"

print(ipv4_validation('1000.1000.1000'))                

#find vowel
def is_vowel(char):
    vowels = 'aeiou'
    return char in vowels
print(is_vowel('a'))

