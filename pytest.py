import pytest
from netmiko import ConnectHandler

# Define device connection parameters
device = {
    'device_type': 'cisco_iosxr',
    'ip': '10.1.1.1',
    'username': 'admin',
    'password': 'password'
}

# Define OSPF configuration
ospf_config = '''
router ospf 1
 router-id 1.1.1.1
 network 10.1.1.0 0.0.0.255 area 0
'''

# Define test function
def test_ospf_configuration():
    # Establish connection to device
    with ConnectHandler(**device) as net_connect:
        # Configure OSPF
        net_connect.send_config_set(ospf_config.splitlines())
        
        # Verify OSPF configuration
        output = net_connect.send_command('show running-config router ospf')
        assert 'router ospf 1' in output
        assert 'router-id 1.1.1.1' in output
        assert 'network 10.1.1.0 0.0.0.255 area 0' in output
        
        # Verify OSPF neighbor adjacency
        output = net_connect.send_command('show ospf neighbor')
        assert 'Neighbor ID' in output
        assert 'State' in output
        
        # Verify OSPF routes
        output = net_connect.send_command('show ip route ospf')
        assert 'OSPF' in output

# Run test
pytest.main([__file__])