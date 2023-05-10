import os
from settings import ENC_EXT, KEYS_DIR, RSA_PRIVATE_KEY
import fast_file_encryption as ffe
from pathlib import Path


def decryptRSA(cipher_files):
    print(f'\n[+] Decrypting {len(cipher_files)} files')

    private_key_path = f'{KEYS_DIR}/{RSA_PRIVATE_KEY}'
    private_key = ffe.read_private_key(private_key=Path(private_key_path))
    decryptor = ffe.Decryptor(private_key)

    for cipher_file in cipher_files:
        decrypt_file = cipher_file[:-len(ENC_EXT)]
        decryptor.copy_decrypted(Path(cipher_file), Path(decrypt_file))

        os.remove(cipher_file)
        print(f'[+] {cipher_file} -> {cipher_file[:-len(ENC_EXT)]}')
