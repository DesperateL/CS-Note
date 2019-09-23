from socket import *

proxyAddr = ("localhost",8888)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(proxyAddr)
tcpSerSock.listen(1)



while 1:
    print("Ready to serve...")
    tcpCliSock,addr = tcpSerSock.accept()
    print("Received a connection from:",addr)
    message = tcpCliSock.recv(4096).decode()
    print(message)
    filename = message.split()[1].partition("//")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/"+filename
    print(filetouse)
    try:
        f = open(filetouse[1:],"r")
        outputdata = f.read()
        fileExist = "true"
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        tcpCliSock.send(outputdata.encode())
    except IOError:
        if fileExist=="false":
            tcpProxySock = socket(AF_INET,SOCK_STREAM)
            hostn = filename.replace("www.","",1).partition("/")[0]
            print(hostn)
            try:
                print("connecting %s..."%(hostn))
                tcpProxySock.connect((hostn,80))
                print("connected %s."%hostn)
                tcpProxySock.sendall(message.encode())
                resp = tcpProxySock.recv(4096)
                tcpCliSock.sendall(resp)
                print("send success %s."%hostn)
                
            except:
                print("Illegal request")
        else:
            print("HTTP response message for file not found")
    # tcpProxySock.close()
tcpSerSock.close()
