from pyats import aetest
from genie.testbed import load

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_testbed(self, testbed_name="testbed.yaml"):
        self.testbed = load(testbed_name)
        self.testbed.connect(log_stdout=False)

class ConnectivityTest(aetest.Testcase):
    @aetest.test
    def verify_connectivity(self, testbed):
        for device in testbed.devices.values():
            if not device.connected:
                self.failed(f"Device {device.name} is not connected.")
            else:
                self.passed(f"Device {device.name} is connected.")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, testbed):
        for device in testbed.devices.values():
            if device.connected:
                device.disconnect()

if __name__ == "__main__":
    import argparse
    from pyats.aetest import TestRunner

    parser = argparse.ArgumentParser()
    parser.add_argument("--testbed", required=True, help="Path to the testbed file")
    args = parser.parse_args()

    aetest.main(testbed=args.testbed)
