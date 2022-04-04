#!/usr/bin/env python3
""" module description """

__author__ = "evan wilkerson"
__version__ = "beta-00.00.01"

import os
from cryptography.fernet import Fernet

KEY_FILEPATH = "/home/ejwilkerson/git_repos/network_automation/.key.key"


def decrypt_string(encrypted_unicode_string):
    """ function description """
    if os.path.exists(KEY_FILEPATH):
        with open(KEY_FILEPATH, "rb") as my_key_file:
            key = my_key_file.read()
        fernet = Fernet(key)
        encrypted_byte_string = encrypted_unicode_string.encode()
        password = fernet.decrypt(encrypted_byte_string).decode()
        return password
    print("key file not found")
    return None
