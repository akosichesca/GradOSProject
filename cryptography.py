#!/usr/bin/env python2
import time
import sys
import os
import subprocess
from Crypto.Cipher import AES, DES3, ARC4
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

message= ""

def read(filename):
    global message
    with open(filename, 'rb') as f:
        message = f.read()

def encryptFunc(scheme):
    global message
    key = '0123456789abcdef'
    if scheme == "AES":
        IV = 16 * '\x00'
        text2 = '\0' * (16-len(message)%16)
        text = message + text2    
        encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    elif scheme == "DES3":
        IV = 8 * '\x00'          
        text2 = '\0' * (8-len(message)%8)
        text = message + text2    
        encryptor = DES3.new(key, DES3.MODE_CBC, IV=IV)
    elif scheme == "ARC4":
        IV = 8 * '\x00'          
        text = message 
        encryptor = ARC4.new(key)
    message = text
    return encryptor.encrypt

def decryptFunc(scheme):
    global message
    key = '0123456789abcdef'
    if scheme == "AES":
        IV = 16 * '\x00'
        decryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    elif scheme == "DES3":
        IV = 8 * '\x00'
        decryptor = DES3.new(key, DES3.MODE_CBC, IV=IV)
    elif scheme == "ARC4":
        IV = 8 * '\x00'
        message = message
        decryptor = ARC4.new(key)
    return decryptor.decrypt

import socket
def sendFunc():
    global message
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.1.171', 10000)
    sock.connect(server_address)
    sock.sendall(message)
    sock.close

from multiprocessing import Process, Lock, Pipe
def execFunc(function, message, locklock, lock, conn):
    lock.acquire()
    locklock.release()
    message = function(message)
    lock.release()
    conn.send(message)
    conn.close()

def monitor(function, outFile):
    global message
    startTime = int(time.time() * 1000)
    parent_conn, child_conn = Pipe()
    locklock = Lock()
    locklock.acquire()
    lock = Lock()
    p = Process(target=execFunc, args=(function, message, locklock, lock, child_conn))
    p.start()
    locklock.acquire()
    with open(outFile, 'w') as f:
        while not lock.acquire(block=False):
            output = '{} {}'.format(int(time.time() * 1000) - startTime, subprocess.check_output("ps --no-headers -o '%cpu,%mem' -p {}".format(p.pid), shell=True).strip())
            print(output)
            f.write(output + '\n')
            time.sleep(.01)
    message = parent_conn.recv()
    p.join()


pi = 'pi2'
OS = 'raspbian'
schemes = ['AES', 'DES3', 'ARC4']
files = ['1MB', '2MB', '3MB', '4MB', '5MB', '10MB', '15MB', '20MB', '25MB', '30MB', '35MB', '40MB']
outDir = 'results'

# Ensure outDir exists
subprocess.call('mkdir {}'.format(outDir), shell=True)

for scheme in schemes:
    for f in files:
        print('Reading {}'.format(f))
        read(f)
        print('Encrypting {} using {} on a {} running {}'.format(f, scheme, pi, OS))
        monitor(encryptFunc(scheme), outDir + '/{}-{}-{}-{}-{}.dat'.format(pi, OS, scheme, f, 'encrypt'))
        print('Decrypting {} using {} on a {} running {}'.format(f, scheme, pi, OS))
        monitor(decryptFunc(scheme), outDir + '/{}-{}-{}-{}-{}.dat'.format(pi, OS, scheme, f, 'decrypt'))
        #print('Sending message')
        #monitor(sendFunc(), outDir + '/{}-{}-{}-{}.dat'.format(pi, OS, f, 'upload'))
