#!/usr/bin/env python3
""" module description """

__author__ = "evan wilkerson"
__version__ = "beta-00.00.01"

import os
from cryptography.fernet import Fernet


SECRET = "gAAAAABiRax5hP0y0K2tFppot7lEPgbn3kaFfhDfc9hY25BooNsxaSAsIU27YES1wA9W9jjamyAThJc3I77sh32MsoAiLHFGOPnvqjmke4kgNmDgcxh94yA="
KEY_FILEPATH = "/home/bodayngo/git_repos/network_automation/code/.key.key"


def decrypt_string(encrypted_unicode_string):
    """ function description """
    if os.path.exists(KEY_FILEPATH):
        with open(KEY_FILEPATH, "rb") as my_key_file:
            key = my_key_file.read()
        fernet = Fernet(key)
        encrypted_byte_string = encrypted_unicode_string.encode()
        password = fernet.decrypt(encrypted_byte_string).decode()
        return password
    else:
        print("key file not found")


def main():
    """function docstring"""
    password = decrypt_string(SECRET)
    print(password)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nuser has exited script")
