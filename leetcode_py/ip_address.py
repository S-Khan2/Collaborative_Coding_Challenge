"""
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example,  "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses 
        while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses."""

def validate_ipv4(string: str):
    # "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros

    ipv4_parts = string.split('.')
    if len(ipv4_parts) != 4:
        return False
    
    for ipv4_part in ipv4_parts:
        if ipv4_part[0] ==  '0' and ipv4_part != '0':
            return False
        try:
            num = int(ipv4_part)
            if num <0 or num>255:
                return False
        except:
            return False
    return True
