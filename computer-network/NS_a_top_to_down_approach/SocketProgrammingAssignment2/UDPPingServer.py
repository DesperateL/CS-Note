import random

from socket import *

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('localhost',12000))
while True:
    rand = random.randint(0,10)
    message,addr = serverSocket.recvfrom(1024)
    message = message.upper()
    print("Receive:",message.decode())
    if rand<4:
        continue

    serverSocket.sendto(message,addr)