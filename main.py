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
    print("[?] Select Test Type")
    print("[1] RSA-1024")
    print("[2] AES-256")
    print("[3] Benchmark Test")
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
        start_time = time.time()
        encryptRSA(normal_files)
        rsa_encryption_time = time.time() - start_time
        rsa_decription_start_time = time.time()
        print(
            f"\n[+] Time passed: {rsa_encryption_time} seconds in RSA Encryption/Benchmark mode")
        (normal_files, encrypted_files) = getFiles(TARGET_DIR)
        decryptRSA(encrypted_files)
        rsa_decription_time = time.time() - rsa_decription_start_time
        print(
            f"\n[+] Time passed: {rsa_decription_time} seconds in RSA Decryption/Benchmark mode")
        rsa_total_time = time.time() - start_time
        print(
            f"\n[+] Time passed: {rsa_total_time} seconds in RSA Total/Benchmark mode")

        (normal_files, encrypted_files) = getFiles(TARGET_DIR)
        start_time = time.time()
        encryptAES(normal_files)
        aes_encryption_time = time.time() - start_time
        aes_encryption_start_time = time.time()
        print(
            f"\n[+] Time passed: {aes_encryption_time} seconds in AES Encryption/Benchmark mode")
        (normal_files, encrypted_files) = getFiles(TARGET_DIR)
        decryptAES(encrypted_files)
        aes_decryption_time = time.time() - aes_encryption_start_time
        print(
            f"\n[+] Time passed: {aes_decryption_time} seconds in AES Decryption/Benchmark mode")
        aes_total_time = time.time() - start_time
        print(
            f"\n[+] Time passed: {aes_total_time} seconds in AES Total/Benchmark mode")

        print("\n===================")
        print("= RSA Algorithm")
        print("===================")
        print(f"= Encryption Time: {rsa_encryption_time} seconds")
        print(f"= Decryption Time: {rsa_decription_time} seconds")
        print(f"= Total Time: {rsa_total_time} seconds")
        print("===================")
        print("= AES Algorithm")
        print("===================")
        print(f"= Encryption Time: {aes_encryption_time} seconds")
        print(f"= Decryption Time: {aes_decryption_time} seconds")
        print(f"= Total Time: {aes_total_time} seconds")
        print("===================")

    else:
        print("Invalid Choice")
