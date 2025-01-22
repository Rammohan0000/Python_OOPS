from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import unittest


class TestNetmikoConfigChange(unittest.TestCase):
    def setup(self):
        # Device details
        self.device = {
            'device_type': 'cisco_ios',
            'host': '192.168.1.1',
            'username': 'admin',
            'password': 'cisco',
            'port': 22,
        }
        self.connection = ConnectHandler(**self.device)
        self.connection.enable()
    def tearDown(self):
        self.connection.disconnect()
    def test_config_change(self):
        # Send configuration commands
        self.connection.send_config_set(['int loop 0', 'ip address 1.1.1.1 255.255.255.255'])
        output = self.connection.send_command('show ip int brief | inc Loopback0')
        self.assertIn('1.1.1.1', output)
    def test_config_change_fail(self):
        # Send configuration commands
        self.connection.send_config_set(['int loop 0', 'ip address 1.1.1.1 255.255.255.255'])
    def test_config_change_fail(self):
        # Send configuration commands
        self.connection.send_config_set(['int loop 0', 'ip address 1.1.1.1 255.255.255.255'])
        output = self.connection.send_command('show ip int brief | inc Loopback0')
        self.assertIn('1.1.1.1', output)  
if __name__ == "__main__":
    unittest.main()


'''
python -m unittest untest-2.py

'''            
                                                  