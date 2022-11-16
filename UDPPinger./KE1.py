from calendar import month_name
import socket
from socket import*
from time import time, ctime
from datetime import datetime as dt

import sys

sock = socket(AF_INET, SOCK_DGRAM)
serveraddress = ('localhost', 12000)
message = "this is the message"
allRtt = []
packetsLost =0
numberofpackets = 50
sock.settimeout(1)
days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]

for i in range(numberofpackets):
    startTime = time() # Retrieve the current time
    today = dt.today()
    day_name = today.weekday()
    startTime = time() # Retrieve the current time
    mydate = dt.now()
    mydate.strftime("%b")

    message = "Kim " + str(i+1) + " " + days[day_name]+ " " + mydate.strftime("%b") + " " + mydate.strftime("%d") + " " +  ctime(startTime)[11:19] + " " + str(mydate.year)

    try:

        # Sending the message and waiting for the answer
        sock.sendto(message.encode(),serveraddress)
        encodedModified, serverAddress = sock.recvfrom(1024)

        # Checking the current time and if the server answered
        endTime = time()

        rtt = (endTime-startTime)*1000
        allRtt.append(rtt)
        modifiedMessage = encodedModified.decode()
        print("Kim " + str(i+1) +":" "Server Reply:" + modifiedMessage + ",RTT =  %.3f ms" % ((rtt)))

       
    except:
        print("PING %i Request timed out" % (i+1))
        packetsLost +=1

sock.close()
maxRtt = 0
minRtt = 10
totalRtt=0

for item in range(len(allRtt)):
    if allRtt[item]> maxRtt:
        maxRtt = allRtt[item]
    if allRtt[item] < minRtt:
        minRtt = allRtt[item]
    totalRtt+=allRtt[item]

avgRtt = totalRtt/len(allRtt)
percentlost = packetsLost/numberofpackets
print("Min RTT = " ,minRtt)
print("Max RTT = " ,maxRtt)
print("Avg RTT = " ,avgRtt )
print("Packet Loss " + str(percentlost) + "%")
