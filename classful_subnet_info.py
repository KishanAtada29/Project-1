import functions as f

def class_A():
    return 24
def class_B():
    return 16
def class_C():
    return 8

def classful_subnet():
    classful_subnet = {
       'class A':{
           'CIDR': '/8',
           'Number of usable IPs': (2**class_A()) - f.unusable_IPs(),
           'Subnetmask': '255.0.0.0'
       },
       'class B':{
           'CIDR': '/16',
           'Number of usable IPs': (2**class_B()) - f.unusable_IPs(),
           'Subnetmask': '255.255.0.0'
        },
        'class C':{
           'CIDR': '/24',
           'Number of usable IPs': (2**class_C()) - f.unusable_IPs(),
           'Subnetmask': '255.255.255.0'
        }

    }

    for subnetmask, value in classful_subnet.items():
        print('')
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 
