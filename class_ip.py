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

# without regex
def status(interface_data):
    details = []
    for line in interface_data.strip().split("\n"):
        parts = line.split()  # Split by whitespace
        if len(parts) == 3:  # Ensure valid line structure
            interface, ip, state = parts  # Unpack values
            if state.lower() == "up":  # Check if state is "up"
                details.append({"interface": interface, "ip": ip, "state": state})
    return details
interface_data = '''
gigabitethernet0/1  192.168.1.1   up
gigabitethernet0/2  192.168.1.2   down
gigabitethernet0/3  192.168.1.3   down
gigabitethernet0/4  192.168.1.4   up
'''
details = status(interface_data)
for detail in details:
    print(f"Interface: {detail['interface']}, IP: {detail['ip']}, State: {detail['state']}")
