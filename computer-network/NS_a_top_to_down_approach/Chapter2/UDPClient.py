from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET,SOCK_DGRAM)
for i in range(10):
    clientSocket.sendto("?????".encode(),(serverName,serverPort))

clientSocket.close()