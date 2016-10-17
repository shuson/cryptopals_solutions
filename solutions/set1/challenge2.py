#! /usr/bin/env python

"""
Write a function that takes two equal-length hex buffers and produces their XOR combination.
"""

def getHexXor(hexStr1, hexStr2):
    return hex(eval("0x"+hexStr1) ^ eval("0x"+hexStr2))[2:]