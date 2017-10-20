#!/usr/bin/env python2
import sys
from Crypto.Cipher import AES, DES3, ARC4
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

with open(sys.argv[1], 'rb') as f:
    message = f.read()
######## Cryptography  ########
print "Decrypting"
key = '0123456789abcdef'

if sys.argv[2] == "AES":
    IV = 16 * '\x00'        
    decryptor = AES.new(key, AES.MODE_CBC, IV=IV)
elif sys.argv[2] == "DES3":
    IV = 8 * '\x00'          
    decryptor = DES3.new(key, DES3.MODE_CBC, IV=IV)
elif sys.argv[2] == "ARC4":
    IV = 8 * '\x00'          
    message = message 
    decryptor = ARC4.new(key)
else:
    IV = 16 * '\x00'  
    decryptor = AES.new(key, AES.MODE_CBC, IV=IV)



message = decryptor.decrypt(message)
print "Writing"
with open('output', 'wb') as f:
    f.write(message)
###############################
