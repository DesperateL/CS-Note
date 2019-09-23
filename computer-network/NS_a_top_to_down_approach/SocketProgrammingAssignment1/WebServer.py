from socket import *
import threading

def loop(connectionSocket):
    print('thread %s start.' %threading.current_thread().name)
    try:
        message = connectionSocket.recv(1024*1024*1024).decode()
        print(message)
        if len(message.split())<2:
            return
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # todo
        connectionSocket.send("HTTP/1.1 200OK\r\n".encode())
        connectionSocket.send("Content-Length: 600000s\r\n\r\n".encode())

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.close()


serverSocket = socket(AF_INET,SOCK_STREAM)
# todo
serverSocket.bind(("localhost",9009))
serverSocket.listen(10)
while True:
    # todo
    print('Ready to server...')
    connectionSocket,addr = serverSocket.accept()
    t = threading.Thread(target=loop,args=(connectionSocket,))
    t.start()

serverSocket.close()

