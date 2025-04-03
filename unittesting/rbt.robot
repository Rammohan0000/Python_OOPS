*** Settings ***
Library    SSHLibrary
Library    Collections
Library    String

*** Variables ***
${ROUTER_IP}        192.168.1.1
${USERNAME}         admin
${PASSWORD}         cisco123
${OSPF_PROCESS_ID}  1
${NETWORK_1}        192.168.1.0
${WILDCARD_1}       0.0.0.255
${NETWORK_2}        10.10.10.0
${WILDCARD_2}       0.0.0.255
${AREA}             0

*** Test Cases ***
Configure OSPF and Validate
    Open Connection    ${ROUTER_IP}
    Login              ${USERNAME}    ${PASSWORD}
    Enter Configuration Mode
    Configure OSPF
    Save Configuration
    Validate OSPF Configuration
    Close Connection

*** Keywords ***
Enter Configuration Mode
    Write    configure terminal
    Read Until Prompt

Configure OSPF
    Write    router ospf ${OSPF_PROCESS_ID}
    Read Until Prompt
    Write    network ${NETWORK_1} ${WILDCARD_1} area ${AREA}
    Read Until Prompt
    Write    network ${NETWORK_2} ${WILDCARD_2} area ${AREA}
    Read Until Prompt
    Write    exit
    Read Until Prompt

Save Configuration
    Write    write memory
    Read Until Prompt

Validate OSPF Configuration
    Write    show ip ospf neighbor
    ${output} =    Read Until Prompt
    Log    ${output}
    Should Contain    ${output}    FULL    # Ensure OSPF adjacency is established

    Write    show ip route ospf
    ${route_output} =    Read Until Prompt
    Log    ${route_output}
    Should Contain    ${route_output}    O    # Ensure OSPF routes are learned


# to execute with python
# pip install robotframework
# pip install robotframework-pythonlibcore

# python - math_library.py
class MathLibrary:
    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

# robotframework
*** Settings ***
Library  math_library.py

*** Test Cases ***
Addition Test
    ${result}  Add  2  3
    Should Be Equal  ${result}  5

Subtraction Test
    ${result}  Subtract  10  4
    Should Be Equal  ${result}  6

# to run -> robot test_math.robot

