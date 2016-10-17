#! /usr/bin/env python

"""
Convert hex to base64
"""

from binascii import unhexlify, b2a_base64

def hex2base64(hexInput):
    return b2a_base64(unhexlify(hexInput))