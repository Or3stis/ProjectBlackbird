#!/usr/bin/env python3

# probe sniffer
# works for python3

from scapy.all import *

iface = input('\n Enter interface: ')

# creates a list for the probes
# each probe will be documented once
probe_list = []

# print ssid and source of probe request
def handle_packet(packet):
    # looks only for packet with probe request
    if packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11ProbeReq):
        #check the list
        if packet.addr2 not in probe_list:
            probe_list.append(packet.addr2)
            # prints the source mac and the destination
            print (packet[Dot11].addr2 + ' probe to ' + str(packet.info))

print ('Sniffing on', iface, '...\n')
sniff(iface=iface, prn=handle_packet)
