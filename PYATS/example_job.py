# example_job.py

from pyats.easypy import run

def main(runtime):
    # Provide the path to your testbed YAML file
    testbed_file = "testbed.yaml"

    # Run the test script
    run(
        testscript="connectivity_test.py",  # Path to the test script
        runtime=runtime,                   # Runtime environment
        testbed=testbed_file               # Specify the testbed file
    )
