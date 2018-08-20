#Python code to validate the MAC address

import re
mac=raw_input("enter the Mac address :")
valid_mac = re.search('(([0-9a-fA-F])+(:|-)){5}([0-9a-fA-F])+',a)

if valid_mac:
    unicast = re.match('([0-9a-fA-F]+):',a)
    change_form = bin(int(unicast.group(1),16))
    multicast = re.search('([0]$)',change_form)
    if multicast:
        print("Unicast address")
    else:
        print("Multicast address")
else:
    print("Not a valid MAC address")
