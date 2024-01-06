# Hexshift
# A encryption algorithm that uses shifters to cipher hex.
# Github: https://www.github.com/lewisevans2007/hexshift
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import random


def generate_shifter():
    shifter = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    random.shuffle(shifter)
    return shifter

def encrypt(data, shift_times):
    """Encrypts data using hexshift

    Args:
        data (str): The data to encrypt
        shift_times (int): The amount of times to shift the data

    Returns:
        bytes: The encrypted data
        list: The shifters used
    """
    data = data.hex().upper()
    iterate = 0
    shifter = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    shifters = []
    for i in range(shift_times):
        output = ""
        shift_list = generate_shifter()
        shifters.append(shift_list)
        for d in data:
            index = shifter.index(d)
            output = output + shift_list[index]
        data = output
    return bytes(bytearray.fromhex(data)), shifters


def decrypt(data, shifters):
    """Decrypts data using hexshift

    Args:
        data (str): The data to decrypt
        shifters (list): The shifters used to encrypt the data

    Returns:
        bytes: The decrypted data
    """
    data = data.hex().upper()
    shifter = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]
    for s in reversed(shifters):
        output = ""
        for d in data:
            index = s.index(d)
            output = output + shifter[index]
        data = output
    return bytes(bytearray.fromhex(data))
