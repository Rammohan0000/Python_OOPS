#configuration backup test
from netmiko import ConnectHandler
import unittest

class TestBackup(unittest.TestCase):
    def setup(self):
        device = {
            'device_type': 'cisco_ios',
            'host': '192.168.122.1',
            'username': 'cisco',
            'password': 'cisco',
            'port': 22,
        }
        self.connection = ConnectHandler(**device)
        self.connection.enable()
    def test_backup(self):
        output = self.connection.send_command('show run')
        self.assertTrue('version' in output)
        with open('backup.txt', 'w') as file:
            file.write(output)
        with open('backup.txt', 'r') as file:
            self.assertEqual(file.read(), output)

    def teardown(self):
        self.connection.disconnect()

if __name__ == '__main__':
    unittest.main()
    