from socket import *

socketClient = socket(AF_INET,SOCK_STREAM)

socketClient.connect(("localhost",12000))

for i in range(10):
    
    socketClient.send("gfsd".encode())
socket.close()