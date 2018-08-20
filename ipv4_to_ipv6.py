#Pyhton code to convert given ipv4 address to ipvd address

import re

ipv4 = raw_input("enter the IP address :")
ipv6 = []
valid_ip = re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))$',ipv4)

if valid_ip:
    ip_type = re.match('([\d]+).([\d]+).([\d]+).([\d]+)',ipv4)
    byte = [int(ip_type.group(1)),int(ip_type.group(2)),int(ip_type.group(3)),int(ip_type.group(4))]
    for i in range(0,4):
        rem = byte[i] % 16
        quo = int(byte[i] / 16)
        ipv6.append((hex(quo)) + (hex(rem)))

print(" Mapped IPV6 is : 2002:"+(ipv6[0][2])+(ipv6[1][2])+":"+(ipv6[2][2])+(ipv6[3][2])+"::1/64")

