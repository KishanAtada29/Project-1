
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
def octect_value():
    return sum(prefix_bits())
def usable_ip(num):
    num = total_bits() - num
    num = (unusable_IPs() ** num) - unusable_IPs()
    return num