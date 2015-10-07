#!/usr/bin/env python3

import socket
from datetime import datetime
import sys

ip = input('Enter ip: ')
# port = int(input('Enter port: '))
# port_last = int(input('enter last port: '))

# scans the first 1024 ports

# sets initial time of scan
time1 = datetime.now()

try:
    for port in range(1, 1025):

        # opens socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # makes a connection to the port
        result = s.connect_ex((ip, port))

        if result == 0:
            print('Port %s Open', port)
        s.close()

        # end of scan
        time2 = datetime.now()

except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit()

except socket.error:
    print('Could not connect')
    sys.exit()

# display the total time of the scan
time = time2 - time1
print(time)
