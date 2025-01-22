from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import unittest

class TestConnection(unittest.TestCase):
    def test_connection(self):
        device = {
            'device_type': 'cisco_ios',
            'host': '192.168.1.1',
            'username': 'admin',
            'password': 'cisco',
            'port': 22,
        }
        try:
            # Attempt to connect to the device
            net_connect = ConnectHandler(**device)
            self.assertIsNotNone(net_connect.find_prompt(), "Failed to retrieve device prompt")
        except NetmikoTimeoutException:
            self.fail("Connection timed out. Check the device IP or network connectivity.")
        except NetmikoAuthenticationException:
            self.fail("Authentication failed. Check username/password.")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")
        finally:
            # Ensure disconnection
            if 'net_connect' in locals():
                net_connect.disconnect()

if __name__ == "__main__":
    unittest.main()
