'''
#Pyats is Python Automated Test Systems
#Initially, Pyats is designed for test infrastructured for cisco devices(ios, nexus...), later it became a general purpose automation framework.
# Main usecases of pyats is for 
    a. comparing snapshots
    b. generating parsers
    c. validating testbed
    d. configuration
    e. troubleshoting
-> Installation of pyats 
    $ mkdir automation
    $ cd automation
    $ python3 -m venv
    $ pip3 install pyats[full], pyats version update
    $ pip3 install xlrd xlrt xlsxwritter(dependencies)
-> creating testbedfile
    $pyats create testbed interactive --output my_own_testbed.yaml

---> Network Snapshot:-

-> goto the directory where we have testbed file
    $ pyats learn all --testbed-file working-tb.yaml --output all_snapshot

-> to learn a particular feature like ospf, interface and platform...
    $ pyats learn interface ospf platform --testbed-file working_tb.yaml --output working_snapshot

-> for troubleshooting, i have loaded some devices which are not able to ping, those devices i kept in broken-tb.yaml, now i will take snapshot of it and compare with working-tb snapshot, to get changes in network topology
    $ pyats learn interface ospf platform --testbed-file broken-tb.yaml --output broken_snapshot

-> now i will compare these snapshots using
    $ pyats diff working_snapshot broken_snapshot --output diff_snapshot

---> parsers(converts standard output to json format)
    $ pyats parse "show vlan" --testbed-file working-tb.yaml --devices <device-name> --output vlan_data
-> we can use different parsers for each cli command, for more parsers check pyats support page

-> to validate testbed
    $ pyats validate testbed --testbed-file working-tb.yaml
-> to view logs
    $ pyats logs view
-> to view logs of a particular testbed
     $ pyats logs view --testbed-file working-tb.yaml
-> to view logs of a particular testbed and device
     $ pyats logs view --testbed-file working-tb.yaml --device <device-name>
-> to view logs of a particular testbed and device and feature
    $ pyats logs view --testbed-file working-tb.yaml --device <device-name> --feature <feature-name>  
-> we can use genie instead of pyats, it is a subset of pyats, it is used for parsing and configuration
-> to create a project in genie
    $ genie create project my_project <project-name><testcase-name> 
-> to create a testbed in genie
    $ genie create testbed <testbed-name> --path <path-to-testbed-file>
-> to create a parser in genie
    $ genie create parser <parser-name> --testbed <testbed-name> --output <output-file> 
-> to get html report
    $ pyats run job <job-name> --html-logs <path-to-html-file>
-> to get json report
    $ pyats run job <job-name> --json-logs <path-to-json-file>
-> in detail logs
    $pyats run job <job-name> --loglevel=debug

'''

# programming
from genie.testbed import load
testbed = load('working-tb.yaml')
device = testbed.devices['nx-osv-1']
device.connect()
output = device.execute('show version')
print(output)

# parsers
from pprint import pprint
parsed = device.parse('show version')
pprint(parsed)

parsed2 = device.parse('show vrf')
pprint(parsed2)
parsed2['vrfs']['default']['vrf_id']
parsed2['vrfs']['default']['vrf_state']
for vrf in parsed2['vrfs']:
    vrf_id = parsed2['vrfs'][vrf]['vrf_id']
    vrf_state = parsed2['vrfs'][vrf]['vrf_state']
    print('Vrf {vrf} is {state}'.format(vrf=vrf_id, state=vrf_state))

# configuration
configuration = [
'interface ethernet2/1'
'shutdown'
]
output = device.configure(configuration)

# learn device configuration in dictionary format
output = device.learn('interfacce')
pprint(output.info)


   

