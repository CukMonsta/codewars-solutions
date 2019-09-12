"""
Extend the string object(JS) or create a function(python, C#) that converts
the value of the string to and from Base64 using the ASCII(UTF-8 for C#)
character set.

Do not use built in functions.

Note: you can learn more about Base64 encoding and decoding here,
https://en.wikipedia.org/wiki/Base64

Note: This kata uses the non-padding version ('=' is not added to the end).
"""

# My Answer with built functions
def to_base_64(string):
    string = string.encode("base64").replace('\n', '')
    if '==' in string:
        return string.replace('==', '')
    else:
        return string.replace('=', '')

def from_base_64(string):
    return string.decode("base64")

# My Answer without built functions
ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_base_64(string):
    binarystr = ''
    encoded = []
    for ch in string:
        # Concatenate 8 binary digits for each source character:
        eightbits = str(bin(ord(ch)))[2:]     # cut unwanted '0b'
        eightbits = eightbits.rjust(8,'0')
        binarystr += eightbits

    # Pad right end:
    if len(binarystr)%6 != 0:
        binarystr = binarystr + '0'*(6 - len(binarystr)%6)

    # Take 6-byte chunks and look them up in ALPH:
    while len(binarystr) >= 6:
        encoded.append(binarystr[:6])
        binarystr = binarystr[6:]

    return ''.join([ALPH[int(x,2)] for x in encoded])


def from_base_64(string):
    binarystr = ''
    decoded = []
    for ch in string:
        # Look up in ALPH and convert to binary:
        sixbits = str(bin(ALPH.index(ch)))
        sixbits = sixbits[sixbits.index('b')+1:]    # cut unwanted '0b'
        sixbits = sixbits.rjust(6,'0')
        binarystr += sixbits

    # Take 8-byte chunks and convert to ASCII chars:
    while len(binarystr) >= 8:
        decoded.append(binarystr[:8])
        binarystr = binarystr[8:]

    return ''.join([unichr(int(x,2)) for x in decoded])

# Best Answer
from base64 import b64encode, b64decode

def to_base_64(string):
    return b64encode(string).replace("=", '')

def from_base_64(string):
    return b64decode(string + "==")

# Tests Suite
Test.describe("Basic tests")
tests = [["this is a string!!","dGhpcyBpcyBhIHN0cmluZyEh"],
  ["this is a test!","dGhpcyBpcyBhIHRlc3Qh"],
  ["now is the time for all good men to come to the aid of their country.","bm93IGlzIHRoZSB0aW1lIGZvciBhbGwgZ29vZCBtZW4gdG8gY29tZSB0byB0aGUgYWlkIG9mIHRoZWlyIGNvdW50cnku"],
  ["1234567890  ", "MTIzNDU2Nzg5MCAg"],
  ["ABCDEFGHIJKLMNOPQRSTUVWXYZ ", "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVog"],
  ["the quick brown fox jumps over the white fence. ","dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4g"],
  ["dGhlIHF1aWNrIGJyb3duIGZveCBqdW1wcyBvdmVyIHRoZSB3aGl0ZSBmZW5jZS4","ZEdobElIRjFhV05ySUdKeWIzZHVJR1p2ZUNCcWRXMXdjeUJ2ZG1WeUlIUm9aU0IzYUdsMFpTQm1aVzVqWlM0"],
  ["VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFna","VkZaU1NtVnJOVVZXVkVwUFpXMWpNVlJWVGtKYWVVRm5h"],
  ["TVRJek5EVTJOemc1TUNBZyAg","VFZSSmVrNUVWVEpPZW1jMVRVTkJaeUFn"]]

for test in tests:
  result=to_base_64(test[0])
  Test.assert_equals(result, test[1])
  Test.assert_equals(from_base_64(result), test[0])
