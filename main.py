
import functions as f
import classful_subnet_info as csi

def manual():
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))
    octect = 0
    subnetmask = []
    if cidr == 0:
        subnetmask = [0,0,0,0]
        print('')
        print(f'Address: {".".join(map(str,(subnetmask)))} /{cidr}')
        print(f'Total IPv4 Address: {f.usable_ip(cidr) + f.unusable_IPs()} ')
        print('Description: /0 represents all IPv4 address and is commonly used as a default route')
    else:
        octet_side = cidr % f.single_octet_bits()
        each_octet = int(cidr / 8)
        for bit in range(each_octet):
            subnetmask.append(sum(f.prefix_bits()))
        for bit in range(octet_side):
            octect = f.prefix_bits()[bit] + octect
        subnetmask.append(octect)
        if len(subnetmask) == 3:
            subnetmask.append(0)
        elif len(subnetmask) == 2:
            subnetmask.append(0)
            subnetmask.append(0)
        elif len(subnetmask) == 1:
            subnetmask.append(0)
            subnetmask.append(0)
            subnetmask.append(0)
        elif len(subnetmask) == 5:
            subnetmask.pop()


        print(f'CIDR: /{cidr}')
        print(f'Nuber of useable host: {f.usable_ip(cidr)}')
        print(f'Subnetmask: {".".join(map(str,(subnetmask)))}')

        

        
        



while True:
    print('')
    print('Subnetmask Planner')
    print('-------------------')
    print('')
    print('1. Claseful Subnet Info')
    print('2. Manual CIDR Calculator')
    print('3. Exit')
    print('')
    user_choice = int(input('Please Enter One of the Choice (1-3): '))
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        print('Invalid option...')
        print('1. Claseful Subnet Info')
        print('2. Manual CIDR Calculator')
        print('3. Exit')
        print('')
        user_choice = int(input('Please Enter One of the Choice (1-3): '))

    
    


    if user_choice == 1:
        csi.classful_subnet()
    elif user_choice == 2:
        manual()
        
    elif user_choice == 3:
        print('Goodbye !')
        break
    print('')
    input('Press Enter to continue...')


