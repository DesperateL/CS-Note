from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM)
# todo
serverSocket.bind(("localhost",9009))
serverSocket.listen(1)
while True:
    # todo
    print('Ready to server...')
    connectionSocket,addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024*1024*1024).decode()
        print(message)
        if len(message.split())<2:
            continue
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # todo
        connectionSocket.send("HTTP/1.1 200OK\r\n".encode())
        connectionSocket.send("Content-Type: html\r\n".encode())
        connectionSocket.send("Content-Length: 600000\r\n\r\n".encode())

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.close()
serverSocket.close()

