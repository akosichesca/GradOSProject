
import socket
import sys
from Crypto.Cipher import AES

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.171', 50000)


#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
data2 = ""

while True:
    # Wait for a connection
    #print >>sys.stderr, 'waiting for a connection'
    try:
        connection, client_address = sock.accept()
        #print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            #data2 = data2 + data
           # print >>sys.stderr, 'received "%s"' % data
            if data:
                pass
                #print >>sys.stderr, 'sending data back to the client'
                #connection.sendall(data)
            else:
                #print >>sys.stderr, 'no more data from', client_address

    	    	## CRYPTOGRAPHY ##########
	    	#key = '0123456789abcdef'
	    	#IV = 16 * '\x00'        
	    	#decryptor = AES.new(key, AES.MODE_CBC, IV)
	    	#data = decryptor.decrypt(data2)
		#print(data)
	    	#data2 = ""
                ###########################    
                break
    finally:
        # Clean up the connection
        connection.close()
