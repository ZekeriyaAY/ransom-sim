import hashlib
import os
from settings import KEYS_DIR, AES_KEY


def generateAESKey(password):
    hasher = hashlib.sha256(password.encode('utf-8'))
    with open(f'{KEYS_DIR}/{AES_KEY}', mode='wb') as p:
        p.write(hasher.hexdigest().encode('utf-8'))

    print(f'\n[+] AES Key Generated and saved in {os.getcwd()}/{KEYS_DIR}/')
    print(f'[+] AES Key: {os.getcwd()}/{KEYS_DIR}/{AES_KEY}')
