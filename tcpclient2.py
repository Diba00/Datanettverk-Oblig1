from socket import *
import sys

# Check if the correct number of arguments were provided
if len(sys.argv) != 4:
    print("Usage: python3 tcpclient.py <serverName> <serverPort> <fileName>")
    sys.exit()

# Get the command-line arguments
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

# Construct the request string
request = "GET /" + fileName + " HTTP/1.1\r\n\r\n"

# Create a TCP socket and connect to the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


# Send the request to the server
clientSocket.send(request.encode())

# Receive the response from the server
#response = clientSocket.recv(4096)

response = clientSocket.recv(4096)

output=""

while len(response) > 0:
    response = clientSocket.recv(4096).decode()
    output += response
print(output)

# Print the response to the console
"""
while len(response) > 0:
    print(response.decode())
    response = clientSocket.recv(4096)
"""

# Close the socket
clientSocket.close()