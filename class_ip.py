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

#write a program to get the ip address of the system
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP Address of the system is {ip_address}")

# write a python program to get details of the interface, which are in up state
def get_up_interfaces(interfaces):
    up_interfaces = []
    for name, details in interfaces.items():
        if details.get('state') == 'up':
            up_interfaces.append({name: details})
    return up_interfaces


# Sample interface data
interfaces = {
    "GigabitEthernet0/0": {"state": "up", "ip": "192.168.1.1", "speed": "1Gbps"},
    "GigabitEthernet0/1": {"state": "down", "ip": "192.168.1.2", "speed": "1Gbps"},
    "FastEthernet0/0": {"state": "up", "ip": "10.0.0.1", "speed": "100Mbps"},
}

# Get interfaces in the 'up' state
up_interfaces = get_up_interfaces(interfaces)

# Print the result
if up_interfaces:
    print("Interfaces in 'up' state:")
    for interface in up_interfaces:
        print(interface)
else:
    print("No interfaces are in the 'up' state.")

#using regex
import re

def get_up_interfaces(interface_output):
    pattern = r"(?P<interface>\S+)\s+\S+\s+up"
    matches = re.finditer(pattern, interface_output)
    up_interfaces = [match.group("interface") for match in matches]
    return up_interfaces


# Example interface output from a network device
interface_output = """
GigabitEthernet0/0   192.168.1.1   up
GigabitEthernet0/1   192.168.1.2   down
FastEthernet0/0      10.0.0.1      up
FastEthernet0/1      10.0.0.2      down
"""

# Get interfaces in 'up' state
up_interfaces = get_up_interfaces(interface_output)

# Print the result
if up_interfaces:
    print("Interfaces in 'up' state:")
    for interface in up_interfaces:
        print(interface)
else:
    print("No interfaces are in the 'up' state.")
