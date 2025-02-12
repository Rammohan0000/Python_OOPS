from pyats import aetest
from pyats.topology import loader

class CommonSetup(aetest.CommonSetup):
    """Common Setup Section - Load Testbed & Connect to Device"""

    @aetest.subsection
    def connect_to_device(self, testbed):
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['router1']
        self.device.connect()
        aetest.loop.mark(VerifyOSPF, device=self.device)

class VerifyOSPF(aetest.Testcase):
    """Test Case to Verify OSPF Configuration"""

    @aetest.setup
    def setup(self, device):
        """Setup: Collect OSPF Neighbor Data"""
        self.ospf_data = device.parse("show ip ospf neighbor")

    @aetest.test
    def check_ospf_neighbors(self, device):
        """Check OSPF Neighbor State"""
        if self.ospf_data and "ospf-neighbor-information" in self.ospf_data:
            self.passed("OSPF neighbors found")
        else:
            self.failed("No OSPF neighbors found")

    @aetest.test
    def verify_ospf_interfaces(self, device):
        """Verify OSPF Interfaces"""
        ospf_interfaces = device.parse("show ip ospf interface")
        if ospf_interfaces:
            self.passed(f"OSPF Interfaces: {list(ospf_interfaces.keys())}")
        else:
            self.failed("No OSPF interfaces found")

class CommonCleanup(aetest.CommonCleanup):
    """Cleanup Section - Disconnect Device"""

    @aetest.subsection
    def disconnect_device(self, testbed):
        self.device.disconnect()

if __name__ == "__main__":
    aetest.main()
