#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import socket module
from socket import socket, AF_INET, SOCK_STREAM

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', 8081))
serverSocket.listen(1)

while True:
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()

        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
    except IOError:

        connectionSocket.send('file not found')
    finally:
        connectionSocket.close()


serverSocket.close()
