#import socket module
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

try:
    while True:
        #Establish the connection
        print('Ready to serve')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()

            if not message.strip():
                connectionSocket.close()
                continue

            request_parts = message.split()
            if len(request_parts) < 2:
                connectionSocket.send("HTTP/1.1 400 Bad Request\r\n\r\n".encode())
                connectionSocket.close()
                continue

            filename = request_parts[1]
            filepath = filename.lstrip('/')
            
            f = open(filepath, 'r')
            outputdata = f.read()
            f.close()

            #Send 2 HTTP header lines into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode()) #Explicitly tells the browser that the file is HTML, I had issues without this line

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()

        except IOError:
            #Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><body><h1>404 - Not Found</h1></body></html>".encode())

            #Close client socket
            connectionSocket.close()
    
except KeyboardInterrupt:
    print("\nShutting down server...")
    serverSocket.close()
    sys.exit

serverSocket.close()
sys.exit()