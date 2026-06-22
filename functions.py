"""Contains shared helper functions for IPv4 and CIDR calculations."""

import subnetmask_calculator as sc

def prefix_bits():
    """Return the bit values used to calculate one subnet-mask octet."""
    numbers = [128, 64, 32, 16, 8, 4, 2, 1]
    return numbers

def single_octet_bits():
    """Return the number of bits in one IPv4 octet."""
    return len(prefix_bits())

def number_of_octets():
    """Return the number of octets in an IPv4 address."""
    return 4

def total_bits():
    return (single_octet_bits() * number_of_octets())


  
def unusable_IPs():
    """Return the 2 traditionally reserved network and broadcast addresses."""
    return 2

def octect_value():
    """Return the maximum decimal value of one IPv4 octet."""
    return sum(prefix_bits())

def usable_ip(num):
    """
    Calculate the number of usable IPv4 host addresses.

    Args:
        num: The CIDR prefix.

    Returns:
        The number of usable host addresses.
    """
    num = total_bits() - num
    num = (unusable_IPs() ** num) - unusable_IPs()
    return num


def get_result(cidr,desc):
    """
    Display the calculated CIDR information.

    Args:
        cidr: An integer from 0 to 32.
        desc: A description of the CIDR prefix.
    """
    if cidr == 31:
        ip = 2
    elif cidr == 32:
        ip = 1
    else: 
        ip = usable_ip(cidr)
        
    print(f'CIDR: /{cidr}')
    print(f'Number of useable host: {ip}')
    print(f'Subnet Mask: {".".join(map(str,(sc.subnetmask_calculator(cidr))))}')
    print('Description: ' + desc)
def display_menu():
    print('1. Claseful Subnet Info')
    print('2. Manual CIDR Calculator')
    print('3. Exit')
