#!/usr/bin/env python3
""" module description """

__author__ = "evan wilkerson"
__version__ = "beta-00.00.01"

from crypto_lib import decrypt_string

SECRET = (
    "gAAAAABiRax5hP0y0K2tFppot7lEPgbn3kaFfhDfc9hY25BooNsxaSAsIU27YE"
    "S1wA9W9jjamyAThJc3I77sh32MsoAiLHFGOPnvqjmke4kgNmDgcxh94yA="
)


def main():
    """ function docstring """
    password = decrypt_string(SECRET)
    print(password)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nuser has exited script")
