from pyats.aetest import Testcase, test, step

class MyTestcase(Testcase):
    @test
    def test_steps_example(self):
        with step.start("Check if number is even"):
            number = 4
            assert number % 2 == 0
            step.passed()  # Marks the step as passed if no error occurs

        with step.start("Check if number is negative"):
            number = 4
            if number < 0:
                step.passed()
            else:
                step.failed()  # Marks the step as failed

# Run the test manually (if needed)
if __name__ == "__main__":
    import pyats.aetest
    pyats.aetest.main()
