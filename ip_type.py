ip = raw_input("Enter an ip address : ")
oct = ip.split('.')

for i in range (0,4):   #Logic to identify the input is a valid ip or not
    if(oct[i].isdigit() == False):
        print "Invalid ip address"
        break
    if(len(oct[i]) == 0 or len(oct[i]) > 3):
        print "Invalid ip address"
        break
    if(int(oct[i]) > 255):
        print "Invalid ip address"
        exit(0)

if(int(oct[3]) == 0):
    print "Network Address"
    exit(0)

if (int(oct[0]) <= 223):
    if(int(oct[3]) == 255):
        print "Broadcast Address"
    elif(int(oct[0]) == 127 and int(oct[3]) == 255):
        print "Broadcast Address"
    elif(int(oct[0]) == 127):
        print "Loopback Address"
    else:
        print "Unicast Address"

if (int(oct[0]) >= 224):
    if(int(oct[0]) <= 239 and int(oct[3]) == 255):
        print "Broadcast Address"
    elif(int(oct[0]) <= 239):
        print "Multicast Address"

if (int(oct[0]) >= 240):
    if(int(oct[0]) <= 255 and int(oct[3]) == 255):
        print "Broadcast Address"
    else:
        print "Reserved Address"
