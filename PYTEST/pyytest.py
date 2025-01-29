from netmiko import ConnectHandler
import pytest

# Device details
DEVICE = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'cisco',
    'port': 22,
}

@pytest.fixture(scope="module")
def netmiko_connection():
    """
    Pytest fixture to establish and return a Netmiko connection.
    Ensures the connection is closed after tests.
    """
    connection = ConnectHandler(**DEVICE)
    yield connection
    connection.disconnect()

def test_ospf_configuration(netmiko_connection):
    """
    Test case to configure and validate OSPF on a Cisco device.
    """
    # Step 1: OSPF Configuration Commands
    ospf_config_commands = [
        'router ospf 1',
        'network 10.0.0.0 0.0.0.255 area 0',
        'network 192.168.1.0 0.0.0.255 area 0',
    ]
    netmiko_connection.send_config_set(ospf_config_commands)

    # Step 2: Verify OSPF Configuration
    verification_command = "show running-config | section router ospf"
    output = netmiko_connection.send_command(verification_command)

    assert 'router ospf 1' in output, "OSPF process 1 not configured."
    assert 'network 10.0.0.0 0.0.0.255 area 0' in output, "OSPF network 10.0.0.0/24 not configured."
    assert 'network 192.168.1.0 0.0.0.255 area 0' in output, "OSPF network 192.168.1.0/24 not configured."

def test_ospf_neighbors(netmiko_connection):
    """
    Test case to validate OSPF neighbor relationships.
    """
    verification_command = "show ip ospf neighbor"
    output = netmiko_connection.send_command(verification_command)

    # Ensure at least one OSPF neighbor is in the "Full" state
    assert "Full" in output, "No OSPF neighbors in the Full state."


'''
To run the test cases, execute the following command:
pytest -v pyytest.py
'''