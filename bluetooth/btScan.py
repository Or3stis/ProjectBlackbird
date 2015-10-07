#!/usr/bin/env python3

# python3
# scans for bluetooth devices every 3 seconds

import time
from bluetooth import *

# create empty list to store mac addresses
mac_list = []

# create the txt file
blue_mac_target = 'blue_mac_target.txt'


def findDevs():
    # scans for bluetooth devices
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in mac_list:
            f = open(blue_mac_target, 'w')
            mac_list.append(addr)
            f.write(str(mac_list))
            f.close()
            print('[*] Found Bluetooth Device: '+str(name))
            print('[*] mac address: '+str(addr))

# scans every 3 seconds
while True:
    findDevs()
    time.sleep(3)

print('mac_target.txt has been populated.')
input('Press enter to continue.')
#!/usr/bin/env python3

# python3
# scans for bluetooth devices every 3 seconds

import time
from bluetooth import *

# create empty list to store mac addresses
mac_list = []

# create the txt file
blue_mac_target = 'blue_mac_target.txt'


def findDevs():
    # scans for bluetooth devices
    foundDevs = discover_devices(lookup_names=True)
    for (addr, name) in foundDevs:
        if addr not in mac_list:
            f = open(blue_mac_target, 'w')
            mac_list.append(addr)
            f.write(str(mac_list))
            f.close()
            print('[*] Found Bluetooth Device: '+str(name))
            print('[*] mac address: '+str(addr))

# scans every 3 seconds
while True:
    findDevs()
    time.sleep(3)

print('mac_target.txt has been populated.')
input('Press enter to continue.')
