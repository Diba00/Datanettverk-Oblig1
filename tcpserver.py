"""

#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
server_port = 1269 #Standard port
serverSocket.bind(("", server_port))
serverSocket.listen(1)

while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    print("du er inne")
    
    try:
        message = connectionSocket.recv(4096).decode()
        print(message)
        filename = message.split()[1]
        #print (filename)
        f = open(filename[1:])
        outputdata = f.read()
        f.close() 
    #Send one HTTP header line into socket
        responseHTTP = "HTTP/1.1 200 OK \r\nContent-Type: text/html\r\nContent-Lenght: " +str(len(outputdata)) + "\r\n\r\n"
        
        connectionSocket.send(responseHTTP.encode()) 

    #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n\r\n".encode()) 
        connectionSocket.close()
    except IOError:
    #Send response message for file not found
        
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.sendall(response.encode())

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
"""
# Import necessary modules
from socket import *
import sys
import threading

# Define a function to handle each client request
def handle_request(connectionSocket):
    try:
        message = connectionSocket.recv(4096).decode()
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close() 
        responseHTTP = "HTTP/1.1 200 OK \r\nContent-Type: text/html\r\nContent-Lenght: " +str(len(outputdata)) + "\r\n\r\n"
        connectionSocket.send(responseHTTP.encode()) 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n\r\n".encode()) 
        connectionSocket.close()
    except IOError:
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.sendall(response.encode())
        connectionSocket.close()

# Create the main thread to listen for client connections
serverSocket = socket(AF_INET, SOCK_STREAM)
server_port = 1269
serverSocket.bind(("", server_port))
serverSocket.listen(1)

while True:
    # Wait for a client to connect
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("du er inne")

    # Create a new thread to handle the client request
    t = threading.Thread(target=handle_request, args=(connectionSocket,))
    t.start()

# Close the server socket and exit the program
serverSocket.close()
sys.exit()
