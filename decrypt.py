#!/usr/bin/env python2
import sys
from Crypto.Cipher import AES

with open(sys.argv[1]) as f:
    message = f.read()
######## Cryptography  ########
print "Decrypting"
key = '0123456789abcdef'
IV = 16 * '\x00'        
decryptor = AES.new(key, AES.MODE_CBC, IV)
message = decryptor.decrypt(message)
print "Writing"
with open('output', 'w') as f:
    f.write(message)
###############################
