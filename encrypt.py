import sys
from Crypto.Cipher import AES

with open('Desktop/4550') as f:
    message = f.read()
######## Cryptography  ########
print "Encrypting"
key = '0123456789abcdef'
IV = 16 * '\x00'          
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)
text2 = '\0' * (16-len(message)%16)
text = message + text2
message = encryptor.encrypt(text)
print "Writing"
with open('output', 'w') as f:
    f.write(message)
###############################
             
