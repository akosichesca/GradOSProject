import socket
import sys
from Crypto.Cipher import AES

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.171', 50000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    #with open('../1MB') as f:
    #    message = f.read()
    #print >>sys.stderr, 'sending "%s"' % message

    ######## Cryptography  ########

    #print "Encrypting"
    #key = '0123456789abcdef'
    #IV = 16 * '\x00'          
    #mode = AES.MODE_CBC
    #encryptor = AES.new(key, mode, IV=IV)
    #text2 = '\0' * (16-len(message)%16)
    #text = message + text2
    #message = encryptor.encrypt(text)
    #print(message)
    ###############################
    message = "1"
    print "Sending"
    sock.sendall(message)

    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)

    print "received"
    
    #while amount_received < amount_expected:
    #    data = sock.recv(16)
    #    amount_received += len(data)
    #    #print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
              
