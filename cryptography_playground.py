#!/usr/bin/env python3
"""
<module_description>
"""

import os
from cryptography.fernet import Fernet


encrypted_password = "gAAAAABiRZ7aSE5kVEK7NVVblLdbZNhZ33ZW9E0bMtA6GsKArAH4cZ2Ts6-oxQIoWIE_NVcHipJbmkirW9TykQ5-w44LBvuXkQ=="


def decrypt_password(encrypted_unicode_string, key_filepath):
    """
    <function_description>

    Parameters
        encrypted_unicode_string (str): <parameter_description>
        key_filepath (str): <parameter_description>

    Returns
        password (str): <return_description>
    """
    if os.path.exists(key_filepath):
        with open(key_filepath, "rb") as my_key_file:
            key = my_key_file.read()
        fernet = Fernet(key)
        encrypted_byte_string = encrypted_unicode_string.encode()
        password = fernet.decrypt(encrypted_byte_string).decode()
        return password
    else:
        print("key file not found")


def main():
    """function docstring"""
    password = decrypt_password(encrypted_password, "./.key.key")
    print(password)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nuser has exited script")
