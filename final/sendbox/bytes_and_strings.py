
import os
import codecs
import hashlib


def bytes_to_str(b):
    s = str(codecs.encode(b,"hex"),"utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    b = codecs.decode(bytes(s,"utf-8"),"hex")
    assert type(b) is bytes
    return b

def generate_credentials(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        #, dklen=128
        )
    print(salt)
    print(key)
    return {
        'salt':bytes_to_str(salt), 
        'key' :bytes_to_str(key),
    }

def verify_password(password, credentials):
    salt = str_to_bytes(credentials['salt'])
    key  = str_to_bytes(credentials['key'])
    print(salt)
    print(key)
    new_key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        #,dklen=128
        )
    return new_key == key

if __name__ == "__main__":
    credentials = generate_credentials("hello")
    print(credentials)
    if verify_password("hello", credentials):
        print('login succeeded')
    else:
        print('login failed')
    if verify_password("fake_password", credentials):
        print('login succeeded')
    else:
        print('login failed')
