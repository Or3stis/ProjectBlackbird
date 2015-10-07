#!/usr/bin/env python3

# ported for python3

from bluetooth import *

addr = str(input('Enter target MAC: '))

def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception:
        print('[-] RFCOMM Port ' + str(port) + ' closed')


for port in range(1, 30):
    rfcommCon(addr, port)
