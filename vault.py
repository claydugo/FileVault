#!/usr/bin/env python3 
"""
Clay Dugo
Febuary 14th 2020
File Vault
CSC 475 
Prof. Sudip Mittal
"""
import argparse, os, secrets, string
from Crypto.Cipher import AES, DES, DES3
try:
    from nonce import *
except ImportError:
    with open('nonce.py', 'w') as n:
        n.write('nonce = None')
    warnings.warn('nonce failed to import and has been created for you, run command again', ImportWarning)

def parse():
    p = argparse.ArgumentParser()
    p.add_argument('file', help='name of the file you want to encrypt/decrpt')
    p.add_argument('key', help='key to use, 8 bytes for DES, 16 bytes for AES, 24 bytes for 3DES')
    a = p.parse_args()
    return a

def e_aes(source, strkey):
    key = strkey.encode()
    data = open(source, 'rb')
    e_cipher = AES.new(key, AES.MODE_EAX)

    nonce = e_cipher.nonce
    ciphertext, tag = e_cipher.encrypt_and_digest(data.read())

    with open(f'{source}.aes', 'wb') as f:
        f.write(ciphertext)

    with open('nonce.py', 'w') as n:
        n.write(f'nonce = {nonce}\ntag = {tag}\n')

    os.remove(f'{source}')
    print(f'Encrypted {source} with AES and key: {key.decode("utf-8")}')

def d_aes(source, strkey, nonce, tag):
    key = strkey.encode()
    with open(source, 'rb') as fa:
        cipher = fa.read()

    d_cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = d_cipher.decrypt(cipher)
    try:
        d_cipher.verify(tag)
        with open(f'{source[:-4]}', 'wb') as f:
            f.write(plaintext)
        print(f'Decrypted {source} with AES')
        os.remove(f'{source}')
    except ValueError:
        print("Key incorrect or message corrupted")

    clearNonce()

def e_DES(source, strkey):
    key = strkey.encode()
    e_cipher = DES.new(key, DES.MODE_EAX)
    data = open(source, 'rb')
    nonce = e_cipher.nonce
    ciphertext = e_cipher.encrypt(data.read())

    with open(f'{source}.des', 'wb') as f:
        f.write(ciphertext)

    with open('nonce.py', 'w') as n:
        n.write(f'nonce = {nonce}\n')

    os.remove(f'{source}')
    print(f'Encrypted {source} with DES and key: {key.decode("utf-8")}')


def d_DES(source, strkey, nonce):
    key = strkey.encode()
    d_cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
 
    with open(source, 'rb') as fa:
        cipher = fa.read()

    try:
        plaintext = d_cipher.decrypt(cipher)
        with open(f'{source[:-4]}', 'wb') as f:
            f.write(plaintext)
        print(f'Decrypted {source} with DES')
        os.remove(f'{source}')
    except ValueError:
        print("Key incorrect or message corrupted")

    clearNonce()

def e_3DES(source, strkey):
    key = strkey.encode()
    e_cipher = DES3.new(key, DES3.MODE_EAX)
    data = open(source, 'rb')
    nonce = e_cipher.nonce
    ciphertext = e_cipher.encrypt(data.read())
    
    with open(f'{source}.3des', 'wb') as f:
        f.write(ciphertext)

    with open('nonce.py', 'w') as n:
        n.write(f'nonce = {nonce}\n')

    os.remove(f'{source}')
    print(f'Encrypted {source} with 3DES and key: {key.decode("utf-8")}')

def d_3DES(source, strkey, nonce):
    d_cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)

    with open(source, 'rb') as fa:
        cipher = fa.read()

    try:
        plaintext = d_cipher.decrypt(cipher)
        with open(f'{source[:-5]}', 'wb') as f:
            f.write(plaintext)
        print(f'Decrypted {source} with 3DES')
        os.remove(f'{source}')
    except ValueError:
        print("Key incorrect or message corrupted")

    clearNonce()

def clearNonce():
    with open('nonce.py', 'w') as n:
        n.write(f'nonce = None\n')

if __name__ == "__main__":
    a = parse()
    key = a.key
    if nonce == None:
        if len(key) == 8:
            e_DES(a.file, key)
        elif len(key) == 16:
            e_aes(a.file, key)
        elif len(key) == 24:
            e_3DES(a.file, key)
        else:
            print('Invalid key format, will generate key to use with AES')
            key = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16))
            e_aes(a.file, key)
    else:
        if len(key) == 8:
            d_DES(a.file, key, nonce)
        elif len(key) == 16:
            d_aes(a.file, key, nonce, tag)         
        elif len(key) == 24:
            d_3DES(a.file, key, nonce)
        else:
            print('Invalid key length, use vault.py -h to see requirements')
    
