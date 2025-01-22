import json
import netmiko

with open('devices.json') as file:
    devices = json.load(file)

with open('commands.txt') as file:
    commands = file.readlines()
    commands = [command.strip() for command in commands]

for device in devices:
    try:
        connection = netmiko.ConnectHandler(**device)
        print(f'Connected to {device["host"]}')
    except netmiko.NetMikoAuthenticationException:
        print(f'Authentication failed for {device["host"]}')
        continue
    except netmiko.NetMikoTimeoutException:
        print(f'Timeout to {device["host"]}')
        continue
    for command in commands:
        print(f'Executing command {command}')
        output = connection.send_command(command)
        print(output)
    connection.disconnect()
    print(f'Disconnected from {device["host"]}')


'''
devices.json
[
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.2",
        "username": "admin",
        "password": "cisco"
    },  
    {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "cisco"
    }
]

commands.txt
show ip int brief
show version
show run

'''


