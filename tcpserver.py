
#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
server_port = 1200 #Standard port
serverSocket.bind(("", server_port))
serverSocket.listen(1)


while True:
#Establish the connection print('Ready to serve...') connectionSocket, addr =
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()
    
    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()
        f.close() 

    #Send one HTTP header line into socket
        
        response =  "HTTP/1.1 200 OK\r\n\r\n" + outputdata
        connectionSocket.send(response.encode())

        connectionSocket.close()

    #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode()) 
        connectionSocket.close()

    except IOError:
    #Send response message for file not found

        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
   
    #Close client socket
    connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
