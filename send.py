#!/usr/bin/python3

import socket
target_ip="0.0.0.0"
target_port=8888
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while TRUE:
    mss=input("enter any input - - ")
    mssenco=mss.encode('ascii')
    s.sendto(mssenco,(target_ip,target_port))


