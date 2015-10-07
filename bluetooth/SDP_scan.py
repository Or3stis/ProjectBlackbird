#!/usr/bin/env python3

# SDP browser
# python3

# TODO add target file option

from bluetooth import *


def sdpBrowse(addr):
    # bluetooth module function for searching the services
    services = find_service(address=addr)
    for service in services:
        # list some of the data
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print('[+] Found ' + str(name) + ' on ' + str(proto) + ':' + port)


sdpBrowse(str(input('Enter MAC address: ')))
# sdpBrowse('FC:19:10:AD:92:2D')
