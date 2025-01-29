# rollback configuration test
# connection testing using unittest
from netmiko import ConnectHandler
import unittest

class TestNetmikoConfigROllback(unittest.TestCase):
    def test_rollback(self):
        device = {
            'device_type': 'cisco_ios',
            'host': '192.168.1.1',
            'username': 'admin',
            'password': 'admin',
            'port': 22,
        }
        self.connection = ConnectHandler(**self.device)
        self.connection.enable()
    def tearDown(self):
        self.connection.disconnect()
    def test_config_rollback(self):
        config_commands = ['int loopback 0', 'ip address 11.11.11.11 255.255.255.255']
        self.connection.send_config_set(config_commands)
        output = self.connection.send_command('show run int loopback 0')
        self.assertIn('11.11.11.11', output)
    # rollback configuration
        rollback_commands = ['config t', 'no int loopback 0']
        self.connection.send_config_set(rollback_commands)
        output = self.connection.send_command('show run int loopback 0')
        self.assertNotIn('11.11.11.11', output)
if __name__=='__main__':
    unittest.main()
                 

        

