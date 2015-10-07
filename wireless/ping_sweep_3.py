#!/usr/bin/env python3

# python 3
# ping sweeper, check for live host in a network using ping
# usage python3 ping_sweep_3.python

import os
import collections
import socket
import subprocess
import sys
import threading
from datetime import datetime

# requesting user input
print('Enter the network address, for example 192.168.1.1')
net = input("> ")

# splitting the address
net1 = net.split('.')
a = "."
net2 = net1[0]+a+net1[1]+a+net1[2]+a

# setting the parameters of the search
print('Enter the starting number, for example 50')
st1 = int(input("> "))
print('Enter the last number')
en1 = int(input("> "))
en1 = en1 + 1

# creatting the dic Dictionary
dic = collections.OrderedDict()

# setting the command
# one packet ping
ping1 = "ping -c 1 "

# to calulate the time of the scan
t1 = datetime.now()


# setting the threads
class myThread (threading.Thread):
    def __init__(self, st, en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en

    def run(self):
        run1(self.st, self.en)


# the main function of the program
def run1(st1, en1):
    # pings each target in the specified range
    for ip in range(st1, en1):
        addr = net2 + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)

        # make a comparison with ping and ttl response
        # every live host is stored in the dic dictionary
        for line in response.readlines():
            if (line.count("ttl")):
                break
        if (line.count("ttl")):
            dic[ip] = addr


total_ip = en1 - st1
tn = 1  # number of ip held from one thread
total_thread = int(total_ip/tn)
total_thread = int(total_thread+1)
threads = []

try:
    for i in range(total_thread):
        en = st1 + tn
        if (en > en1):
            en = en1
        thread = myThread(st1, en)
        thread.start()
        threads.append(thread)
        st1 = en
except:
    print ("error: unable to start thread")


print ("\n active threads:", threading.activeCount())
print ('\nScanning in process...')


for t in threads:
    t.join()
print ("exiting main thread")

# sorting the dic file to print the live hosts
dict = collections.OrderedDict(sorted(dic.items()))
for key in dict:
    print (dict[key], "-->" " live")

t2 = datetime.now()
# calculates the time of the scan
total = t2-t1

print ("scanning completed in ", total)
input('\nPress enter to continue')
