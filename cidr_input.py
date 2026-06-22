"""Handles CIDR input, validates the value, and displays the result."""

import functions as f
import cidr_desc as cd

def cidr_calculator():
    """
    Ask the user for a CIDR prefix and display the subnet information.

    The function validates that the CIDR value is between 0 and 32.
    """
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))


    print('')
    f.get_result(cidr, cd.cidr_desc(cidr))
   
   

