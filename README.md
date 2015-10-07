author: Orestis Mavropoulos

Open-source and free

The code is free to be distributed and altered in any way.

The application is still in its early stages of development.
There are a lot of issues and bugs that need to corrected.

Usage: python3 /project/main.py
Usage instructions are written in each individual program

In order for the .py to function, the topology of the directories should not be changed.

The application is written is for Linux OS. Some of the programs will work on Mac(not tested in Windows), but the full functionality is only for linux.

The purpose of the program is to provide a stress testing toolkit capable to
test devices using wi-fi and bluetooth protocols for communication.
The testing focuses on devices with either small processing power or small
battery life, found usually in Internet of Things environments.

The philosophy of the design is simple. The main program calls either the
wireless attacks or the bluetooth attacks from the corresponding directories.
The user can choose from a number of attacks and programs to stress test the
machines. Each program can function as an independent one. The idea is that the
toolkit can easily be upgraded with added functionality with a simple addition of the
program in the directory and the command to run it, in the .py program.

                        Topology
                           |
                        main.py
                        /     \
                   wireless  bluetooth
                    /   \            \
                   /     \            \
                  /       \            \
            attack1.py  attack2.py    attack3.py

So far the programs are written in python3.

Feedback and recommendations are always welcome. :)
