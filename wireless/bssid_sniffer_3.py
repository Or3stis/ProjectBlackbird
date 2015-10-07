#! /usr/bin/env/ python3

# python 3
# sniffs the ssid and mac and channel
# usage sudo python3 bssid_sniffer.py
# stores the found BSSID in a text file
# the card must be in monitor mode

from scapy.all import *
# import scapy

interface = input('\n Enter the interface: ')
# creating empty list for the data
ap_list = []

# creation of the targer.txt
# the txt will be populated with mac addresses
# of the bssid
target_file = 'mass_target_bssid.txt'


def info(fm):
    # only wireless packets
    if fm.haslayer(Dot11):
        # checks only for beacon packets with type 0
        if ((fm.type == 0) & (fm.subtype == 8)):
            # looks only for new addresses
            if fm.addr2 not in ap_list:
                # appends to the list
                ap_list.append(fm.addr2)

                # populates the .txt with BSSID
                f = open(target_file, 'w')
                f.write(str(fm.addr2))
                f.close()

                print ('SSID:', fm.info, ' BSSID:', fm.addr2,
                       ' Channel:', ord(fm[Dot11Elt:3].info))

# sniff on the chosen interface for the SSID & BSSID
sniff(iface=interface, prn=info)

print('mass_target_bssid.txt has been populated.')
