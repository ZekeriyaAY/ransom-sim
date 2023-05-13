import os
from settings import ENC_EXT, KEYS_DIR, AES_KEY
from Crypto.Cipher import AES


def decryptAES(cipher_files):
    print(f'\n[+] Decrypting {len(cipher_files)} files')
    with open(f'{KEYS_DIR}/{AES_KEY}', mode='rb') as p:
        key = p.read().decode('utf-8')

    key = bytearray.fromhex(key)

    for cipher_file in cipher_files:
        decrypt_file(key, cipher_file)

        os.remove(cipher_file)
        print(f'[+] {cipher_file} -> {cipher_file[:-len(ENC_EXT)]}')


def decrypt_file(key, filename):
    chunksize = 64*1024
    outputFile = filename[:-len(ENC_EXT)]

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)
