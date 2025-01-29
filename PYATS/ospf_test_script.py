from pyats.topology import loader
from pyats.aetest import Testcase, test, main

class OSPFTest(Testcase):
    @test
    def verify_ospf_configuration(self, steps, testbed):
        """
        Verify OSPF Configuration on the Device
        """
        # Load the device from the testbed
        device = testbed.devices['cisco_device']
        device.connect()

        with steps.start("Verify OSPF process ID is configured") as step:
            output = device.execute("show running-config | section router ospf")
            if "router ospf 1" in output:
                step.passed("OSPF process ID 1 is configured.")
            else:
                step.failed("OSPF process ID 1 is NOT configured.")

        with steps.start("Verify OSPF networks are configured") as step:
            if "network 10.0.0.0 0.0.0.255 area 0" in output and \
               "network 192.168.1.0 0.0.0.255 area 0" in output:
                step.passed("OSPF networks are correctly configured.")
            else:
                step.failed("OSPF networks are missing or incorrect.")

        device.disconnect()

    @test
    def verify_ospf_neighbors(self, steps, testbed):
        """
        Verify OSPF Neighbor Relationships
        """
        # Load the device from the testbed
        device = testbed.devices['cisco_device']
        device.connect()

        with steps.start("Verify OSPF neighbors are in Full state") as step:
            output = device.execute("show ip ospf neighbor")
            if "Full" in output:
                step.passed("OSPF neighbors are in Full state.")
            else:
                step.failed("No OSPF neighbors in Full state.")

        device.disconnect()

if __name__ == "__main__":
    # Load testbed and run the test
    testbed = loader.load("testbed.yaml")
    main(testbed=testbed)


'''
Explanation of the Script:
Testbed File:

The testbed.yaml file defines the device's details, such as IP address, OS, and credentials.
Test Script:

The verify_ospf_configuration test verifies if OSPF process ID and networks are configured.
The verify_ospf_neighbors test checks the OSPF neighbor relationships.
PyATS Steps:

steps.start() defines individual verification steps, making the results more detailed and modular.
Device Interaction:

The device is accessed using device.connect().
Commands like show running-config and show ip ospf neighbor are executed for validation.
Test Results:

step.passed() marks the step as successful.
step.failed() marks the step as failed.
How to Run the Test:
Install PyATS:


pip install pyats
Run the Test:


pyats run job ospf_test_script.py --testbed-file testbed.yaml
Sample Output:
Success:
yaml

+------------------------------------------------------------------------------+
| Step Result Summary                                                          |
+------------------------------------------------------------------------------+
| Passed: 2, Failed: 0, Blocked: 0, Skipped: 0, Errored: 0, Aborted: 0         |
+------------------------------------------------------------------------------+
Failure (e.g., Missing OSPF Configuration):
sql

+------------------------------------------------------------------------------+
| Step Result Summary                                                          |
+------------------------------------------------------------------------------+
| Passed: 1, Failed: 1, Blocked: 0, Skipped: 0, Errored: 0, Aborted: 0         |
+------------------------------------------------------------------------------+

+------------------------------------------------------------------------------+
| Failed Steps                                                                 |
+------------------------------------------------------------------------------+
| -> OSPFTest -> verify_ospf_configuration -> Verify OSPF networks are configured
+------------------------------------------------------------------------------+

Advantages of PyATS:

Modular Testing:
Tests are organized into reusable steps.

Detailed Reports:
Generates detailed logs and reports for easy debugging.

Extensibility:
Supports plugins and integrations with Cisco APIs.

Ease of Use:
YAML-based testbed simplifies device management.

This PyATS example provides a robust and scalable way to validate OSPF configurations on network devices.

testbed:
  name: ospf_testbed
  devices:
    cisco_device:
      os: ios
      type: router
      connections:
        defaults:
          class: unicon.Unicon
        cli:
          protocol: ssh
          ip: 192.168.1.1
      credentials:
        default:
          username: admin
          password: cisco
'''
