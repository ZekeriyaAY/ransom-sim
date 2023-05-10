import rsa
import os
from settings import KEYS_DIR, RSA_PUBLIC_KEY, RSA_PRIVATE_KEY


def generateRSAKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open(f'{KEYS_DIR}/{RSA_PUBLIC_KEY}', mode='wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open(f'{KEYS_DIR}/{RSA_PRIVATE_KEY}', mode='wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

    print(f'\n[+] RSA Keys Generated and saved in {os.getcwd()}/{KEYS_DIR}/')
    print(f'[+] Public Key: {os.getcwd()}/{KEYS_DIR}/{RSA_PUBLIC_KEY}')
    print(f'[+] Private Key: {os.getcwd()}/{KEYS_DIR}/{RSA_PRIVATE_KEY}')


# def loadRSAKeys():
#     with open(f'{KEYS_DIR}/{RSA_PUBLIC_KEY}', mode='rb') as p:
#         publicKey = rsa.PublicKey.load_pkcs1(p.read())
#     with open(f'{KEYS_DIR}/{RSA_PRIVATE_KEY}', mode='rb') as p:
#         privateKey = rsa.PrivateKey.load_pkcs1(p.read())

#     print(f'\n[+] RSA Keys Loaded from {os.getcwd()}/{KEYS_DIR}/')
#     print(f'[+] Public Key: {os.getcwd()}/{KEYS_DIR}/{RSA_PUBLIC_KEY}')
#     print(f'[+] Private Key: {os.getcwd()}/{KEYS_DIR}/{RSA_PRIVATE_KEY}')

#     return (publicKey, privateKey)
