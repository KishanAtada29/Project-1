def cidr_desc(cidr):
    if cidr == 0:
        des = '/0 — Represents all IPv4 addresses; commonly used as a default route.'
    elif 1 <= cidr <= 7:
        des = '/1–/7 — Extremely large address ranges, rarely used as normal LAN subnets.'
    elif 8 <= cidr <= 15:
        des = 'Very large networks.'
    elif 16 <= cidr <= 23:
        des = 'Medium-to-large networks.'
    elif 24 <= cidr <= 29:
        des = 'Commonly used for LANs and smaller subnets.'
    elif cidr == 30:
        des = 'Traditionally used for point-to-point links; provides 2 usable hosts.'
    elif cidr == 31:
        des = 'Used for point-to-point links; both are address are used.'
    elif cidr == 32:
        des = 'Represents one specific IPv4 address, often used as a host route.'
    
    return des