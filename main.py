#! /usr/bin/env python3

# python3

# it splits into two functions, one for the wifi testing
# and one for the bluetooth testing


import subprocess

subprocess.call(['clear'])
print("*"*50)
print('''
               PROJECT BLACKBIRD

   A stress testing tool by Orestis Mavropoulos.


''')
print("*"*50)


# the main function
# it requires the user input to choose between
# the interfaces
def main():
    # prints the options of the user
    print("""\nSelect from the menu:

 1)Wi-fi testing mode
 2)Bluetooth testing mode

 99)Exit
""")

    # user input
    choice = int(input('> '))

    if choice == str():
        print('number an int')
        main()
    elif choice == 1:
        subprocess.call(['python3', 'wireless/main_wireless.py'])
    elif choice == 2:
        subprocess.call(['python3', 'bluetooth/main_bluetooth.py'])
    elif choice == 99:
        print('Never forget to use your powers for good. :)\n')
        exit()
    else:
        print('Please enter valid option\n')

    main()

if __name__ == '__main__':
    main()
