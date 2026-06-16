def class_A():
    return 24
def class_B():
    return 16
def class_C():
    return 8
def prefix_bits():
    numbers = [128, 64, 32, 16, 8, 4, 2, 1]
    return numbers
def single_octet_bits():
    return 8
def number_of_octets():
    return 4
def total_bits():
    return (single_octet_bits() * number_of_octets())
def remaing_bits(n):
    return total_bits() - n   
def unusable_IPs():
    return 2
def prefix():
    subnetmasks = {
       'class A':{
           'CIDR': '/8',
           'Number of usable IPs': (2**class_A()) - unusable_IPs(),
           'Subnetmask': '255.0.0.0'
       },
       'class B':{
           'CIDR': '/16',
           'Number of usable IPs': (2**class_B()) - unusable_IPs(),
           'Subnetmask': '255.255.0.0'
        },
        'class C':{
           'CIDR': '/24',
           'Number of usable IPs': (2**class_C()) - unusable_IPs(),
           'Subnetmask': '255.255.255.0'
        }

    }

    for subnetmask, value in subnetmasks.items():
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 

def manual():
    cidr = int(input('Please enter CIDR (0-32): '))
    subnetmask = ''
    prefixList = prefix_bits()
    usableIPs = ((2 ** remaing_bits(cidr)) - unusable_IPs())
    print(f'CIDR: /{cidr}')
    print(f'Number of usbale IPs: {usableIPs}')
        
        






user_choice = input('Please Enter One of the Choice below\nPrefix\tManual\n')
user_choice = user_choice.casefold()
while user_choice != 'prefix' and user_choice != 'manual':
    print('Invalid..')
    user_choice = input('Please Enter One of the Choice below\nPrefix\tManual\n')
    user_choice = user_choice.casefold()


if user_choice == 'prefix':
    prefix()
elif user_choice == 'manual':
    manual()
      


