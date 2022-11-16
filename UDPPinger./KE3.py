# udppingserver with loss and delay
from socket import *
import random
import time
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
while True:
    # Receive the client packet along with the address it is coming from
    rand = random.randint(0,10)
    timedelay = rand/1000
    message, address = serverSocket.recvfrom(1024)
    # The server responds
    if rand < 2:
        continue
    time.sleep(timedelay)
    serverSocket.sendto(message, address)