#!/usr/bin/env python3

# python3

# wireless testing part
# the function of the program is to call independent
# wireless testing programs

import subprocess

print('You have entered the Wi-Fi attack mode.')


# enabling the monitor mode on the wireless card
def EnableMonitorMode():

    interface = str(input('Enter interface: '))

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'iwconfig', interface, 'mode', 'monitor'])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    subprocess.call(['iwconfig'])

    input('Press enter to continue.')


# disabling the monitor mode on the wireless card
def DisableMonitorMode():

    interface = str(input('Enter interface: '))

    subprocess.call(['sudo', 'ifconfig', interface, 'down'])
    subprocess.call(['sudo', 'iwconfig', interface, 'mode', 'managed'])
    subprocess.call(['sudo', 'ifconfig', interface, 'up'])
    subprocess.call(['iwconfig'])

    input('Press enter to continue.')


# changing the mac address of interface
def MacChanger():
    print(' MacChanger function.\n')

    value = int(input(' 1)Random value\n 2)Specific value\n > '))
    interface = str(input(' Enter interface: '))

    if value == 1:
        subprocess.call(['sudo', 'ifconfig', interface, 'down'])
        subprocess.call(['sudo', 'macchanger', '-r', interface])
        subprocess.call(['macchanger', interface])
        subprocess.call(['sudo', 'ifconfig', interface, 'up'])
        input('Press enter to continue.')
    elif value == 2:
        mac = str(input('Enter new mac: '))
        subprocess.call(['sudo', 'ifconfig', interface, 'down'])
        subprocces.call(['sudo', 'ifconfig', interface, 'hw', 'ether', mac])
        subprocess.call(['sudo', 'ifconfig', interface, 'up'])
        input('Press enter to continue.')

    else:
        print('Enter a valid option.\n')
        MacChanger()


# Sniffers
def Sniffer():
    print("""
Select from the menu:

 1) sniff only for mac address of routers(creates target file)
 2) Probe sniffer(Generate target file)
 3) Hidden SSID sniffer(Generate target file)

 99) main menu
""")

    # user input
    choice = int(input('> '))

    # starts the bssid_sniffer_3.py
    if choice == 1:
        subprocess.call(['sudo', 'python3', 'wireless/bssid_sniffer_3.py'])
    elif choice == 2:
        subprocess.call(['sudo', 'python3', 'wireless/probe_sniffer3.py'])
    elif choice == 3:
        subprocess.call(['sudo', 'python3', 'wireless/hidden_ssid.py'])
    elif choice == 99:
        main_wireless()
    else:
        print('Enter a valid option.\n')
        sniffer()


# deauthentication attacks
def DeauthAttack():
    print("""
Select from the menu:

 1) Deauth attack (more options inside the code)
 2) Load saved targets (form the Sniffer option)

 99) Exit for wireless attack menu
""")

    # user input
    choice = int(input('> '))

    if choice == 1:
        subprocess.call(['sudo', 'python3', 'wireless/deauth3.py'])
    elif choice == 99:
        main_wireless()
    else:
        print('Enter a valid option.\n')
        DeauthAttack()


# the main function of the program
# each program is called from the user input
def main_wireless():
    # prints the options of the user
    print("""
Select from the menu:

 1) Check wireless interfaces
 2) Change mac address of the wireless card
 3) Enable monitor mode
 4) Disable monitor mode
 5) Do a ping sweep on the network
 6) Port scanner
 7) Sniffer(require monitor mode)
 8) Deauthentications attacks

 99) main menu
""")

    # user input
    choice = int(input('> '))

    # checking the wireless interfaces
    if choice == 1:
        subprocess.call(['iwconfig'])
        str(input('\nPress enter to continue.'))
    # changing the mac address of the interface
    elif choice == 2:
        MacChanger()
    # enabling the monitor mode
    elif choice == 3:
        EnableMonitorMode()
    # disabling the monitor mode
    elif choice == 4:
        DisableMonitorMode()
    # calls the ping sweep program
    elif choice == 5:
        subprocess.call(['python3', 'wireless/ping_sweep_3.py'])
    # calls the port_scanner program
    elif choice == 6:
        subprocess.call(['python3', 'wireless/port_scanner.py'])
    elif choice == 7:
        Sniffer()
    # deauthentication attacks
    elif choice == 8:
        DeauthAttack()
    # exiting to main menu
    elif choice == 99:
        exit()
    else:
        print('Please enter valid option\n')

    main_wireless()

if __name__ == '__main__':
    main_wireless()
