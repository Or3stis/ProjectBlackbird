#!/usr/bin/env python3

# bluetooth stresstessting tool
# the function of the program is to call independent
# stresstesting bluetooth programs

# hcitool is a linux uitility
# TODO set the interfaces up and down options

import subprocess

print("*"*50)
print('\nYou have entered the Bluetooth attack mode.\n')
print("*"*50)


def main_bluetooth():
    # prints the options of the user
    print("""
Select from the menu:

 1)Checking the Bluetooth Interface
 2)Scan for bluetooth devices(Generates target file)
 3)Scan SDP services
 4)RFcomm scanner
 5)Battery Draining attack

 99)menu
""")

    # user input
    choice = int(input('> '))

    # check for bluetooth interfaces that are up
    if choice == 1:
        subprocess.call(['hcitool', 'dev'])
    # scan for wireless devices
    elif choice == 2:
        subprocess.call(['python3', 'bluetooth/btScan.py'])
    elif choice == 3:
        subprocess.call(['python3', 'bluetooth/SDP_scan.py'])
    elif choice == 4:
        subprocess.call(['python3', 'bluetooth/rfcomm_scan.py'])
    elif choice == 5:
        subprocess.call(['python3', 'bluetooth/dos_bluetooth.py'])
    elif choice == 99:
        exit()
    else:
        print('Enter valid option\n')

    main_bluetooth()

if __name__ == '__main__':
    main_bluetooth()
