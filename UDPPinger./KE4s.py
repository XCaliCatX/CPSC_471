#Server with 20 second timeout/heartbeat

import socket
from socket import AF_INET, SOCK_DGRAM
import random
from time import time

# Create a UDP socket
serverSocket = socket.socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
message = ''
serverSocket.settimeout(20)
while True:
    # Receive the client packet along with the address it is coming from
    try:
        newMessage, address = serverSocket.recvfrom(1024)
        if message != newMessage.decode():
            message = newMessage.decode()
            lastreceived=time()
        currenttime = time()
        time_since = currenttime - lastreceived
        print("Server received: " + newMessage.decode() + " Last Heartbeat received: " + f'{time_since:.4f}' + " seconds ago")
        serverSocket.sendto(newMessage, address)
    except socket.timeout:
        print("No Heartbeat in last 20 seconds")
        print("Server Stops")
        serverSocket.close()
        exit()



