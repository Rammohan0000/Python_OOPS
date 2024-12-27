def is_ip(ip):
    try:
        parts = list(map(int,ip.split('.')))
        if len(parts)!=4 or not all(0<=int(part)<=255 for part in parts):
            return f"{ip} is not a valid ip address"
        if parts[0] == 10 or \
        (parts[0] == 172 and 16 <= parts[1] <=31 ) or \
        (parts[0] == 192 and parts[1] == 168):
            return f'{ip} is an private ip address'
        return f'{ip} is an public ip address'
        
    except ValueError:
        return f'{ip} is not a valid ip address'  

ip_addr = input("Enter the IP Address")
print(is_ip(ip_addr))     

# second method 
import re
def is_ip(ip):
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if not ip_pattern.match(ip):
        return f"{ip} is not a valid ip address"
    parts = list(map(int, ip.split('.')))
    if not all(0 <= part <= 255 for part in parts):
        return f"{ip} is not a valid ip address"
    if parts[0] == 10 or \
        (parts[0] == 172 and 16 <= parts[1] <= 31) or \
            (parts[0] == 192 and parts[1] == 168):
            return f"{ip} is a private ip address"
    return f"{ip} is a public ip address"
ip_addr = input("Enter the IP Address: ")
print(is_ip(ip_addr))

