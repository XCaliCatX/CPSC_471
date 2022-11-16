#client for server with heartbeat
import socket
from socket import*
from time import time, ctime
from datetime import datetime as dt
import calendar
import sys


sock = socket(AF_INET, SOCK_DGRAM)
serveraddress = ('localhost', 12000)
message = "this is the message"
allRtt = []
packetsLost =0
numberofpackets = 1010
sock.settimeout(1)
days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
for i in range(numberofpackets):
    startTime = time() # Retrieve the current time
    today = dt.today()
    day_name = today.weekday()
    mydate = dt.now()
    mydate.strftime("%b")

    message = "Kim Client1: heartbeat at " + days[day_name] + " " + mydate.strftime("%b") + " " + mydate.strftime("%d") +" " +ctime(startTime)[11:19] + " " + str(mydate.year)
    notice = "Kim Client1: sent heartbeat to server at " + days[day_name] + " " +ctime(startTime)[11:19]

    try:
        print(notice)
        # Sending the message and waiting for the answer
        sock.sendto(message.encode(),serveraddress)
        encodedModified, serverAddress = sock.recvfrom(1024)

        # Checking the current time and if the server answered
        endTime = time()
        


       
    except:
        print("PING %i Request timed out" % (i+1))
        packetsLost +=1
