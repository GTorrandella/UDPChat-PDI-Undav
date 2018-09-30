#!/usr/bin/env python3
import sys 
from socket import *

def addPadding(msg):
    while len(msg) < 4:
        msg = msg + " "
    return msg.encode(encoding='utf_8', errors='strict')
  
def countBytes(string):
    """Returns string's length as uft-8 bytes string"""
    return addPadding(str(len(string)))
    
def prepareMessage(string): 
    """Returns the first and second message"""
    string = string.encode(encoding='utf_8', errors='strict')
    stringBytes = countBytes(string)
    return stringBytes, string

def sendMessage(socket, message, direction):
    ms1, ms2 = prepareMessage(message)
    print(ms1, ms2)
    socket.sendto(ms1, direction)
    socket.sendto(ms2, direction)
    
def recvMessage(socket):
    size = socket.recv(4)
    msg, add = socket.recvfrom(int(size))
    return msg, add