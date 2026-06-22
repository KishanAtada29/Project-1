"""Provides and displays classful IPv4 subnet information."""

import functions as f
import subnetmask_calculator as sc


def class_A():
    """
    Return the host-bit and network-bit counts for Class A.

    Returns:
        A tuple containing host bits and network bits.
    """
    network_portion = f.single_octet_bits() * 1
    host_portion = f.single_octet_bits() * 3
    return host_portion, network_portion
def class_B():
    """
    Return the host-bit and network-bit counts for Class B.

    Returns:
        A tuple containing host bits and network bits.
    """
    network_portion = f.single_octet_bits() * 2
    host_portion = f.single_octet_bits() * 2
    return host_portion, network_portion
def class_C():
    """
    Return the host-bit and network-bit counts for Class C.

    Returns:
        A tuple containing host bits and network bits.
    """
    network_portion = f.single_octet_bits() * 3
    host_portion = f.single_octet_bits() * 1
    return host_portion, network_portion

# In a subnet mask, 1 represensts the network portion and 0 represents the host portion
# class_x [0] = host side
# class_x [1] = network side  

def classful_subnet():
    """
    Display Class A, Class B, and Class C subnet information.

    The function shows the default CIDR prefix, usable hosts,
    and subnet mask for each class.
    """
    a = class_A()
    b = class_B()
    c = class_C()
    classful_subnet = {
       'class A':{
           'CIDR': f'/{a[1]}',
           'Number of usable IPs': (2**a[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(a[1]))))}'
       },
       'class B':{
           'CIDR': f'/{b[1]}',
           'Number of usable IPs': (2**b[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(b[1]))))}'
        },
        'class C':{
           'CIDR': f'/{c[1]}',
           'Number of usable IPs': (2**c[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(c[1]))))}'
        }

    }

    for subnetmask, value in classful_subnet.items():
        print('')
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 
