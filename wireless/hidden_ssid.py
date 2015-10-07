#!/usr/bin/env python3

# hidden SSID sniffer
# python 3

from scapy.all import *

# selection of the interface
iface = str(input('\n Enter interface: '))


# enables scapy to sniff for probes
def handle_packet(packet):
    # scans only for request, response and assosiation probes
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) \
        or packet.haslayer(Dot11AssoReq):
        # prints the SSIDs 
        print('Found SSID ' + packet.info)

# enable sniffing
print('sniffing on ' + iface + '...')
sniff(iface=iface, prn=handle_packet)
