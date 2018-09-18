#!/usr/bin/env python3


def CountBytes(string):
    """Returns string's length as uft-8 bytes string"""
    return str(len(string)).encode(encoding='utf_8', errors='strict')

def PrepareString(string):
    """Returns the first and second message"""
    string = string.encode(encoding='utf_8', errors='strict')
    stringBytes = CountBytes(string)
    return stringBytes, string