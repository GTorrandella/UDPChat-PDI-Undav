#!/usr/bin/env python3


def CountBytes(string):
    """Returns string's length as uft-8 bytes string"""
    return str(len(string)).encode(encoding='utf_8', errors='strict')

def PrepareMessage(string):
    """Returns the first and second message"""
    string = string.encode(encoding='utf_8', errors='strict')
    stringBytes = CountBytes(string)
    return stringBytes, string


def SendMessage(socket, message):
    ms1, ms2 = gp.PrepareMessage(message)
    socket.sendto(ms1, (serverName, serverPort))
    socket.sendto(ms2, (serverName, serverPort))
    
def ReadMessage(socket):
    bt, serverAddress = socket.recv(1)
    message, serverAddress = socket.recv(int(bt))
    return message