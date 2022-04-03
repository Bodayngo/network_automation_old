#!/usr/bin/env python3
""" module docstring """

__author__ = "evan wilkerson"
__version__ = "beta-00.00.01"

import httpx
from cryptography_playground import decrypt_string


SECRET = (
    "gAAAAABiRbjtOp7H_GCiYUYjI7pCkEHGDCWjqBxbhaDoBZgPeBr"
    "l0qMu6dAgNcgJzX5b4MnsBfD68cCvKo-jpR26VWYCAFQ56Q=="
)
URL = (
    "https://sandbox-iosxe-latest-1.cisco.com:443/restconf"
    "/data/Cisco-IOS-XE-native:native/interface/"
)
RESTCONF_HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def main():
    """ function docstring """
    password = decrypt_string(SECRET)
    with httpx.Client() as client:
        response = client.get(
            url=URL, headers=RESTCONF_HEADERS, auth=("developer", password)
        )
    print(response.text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nuser has exited script")
    except RuntimeError:
        print("\nuser has exited script")
    except httpx.ConnectTimeout:
        print("timed out")
    except httpx.ConnectError:
        print("connection error")
