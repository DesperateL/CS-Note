from socket import *
import base64


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver = ("smtp.163.com",25)
fromaddress = "13072190030@163.com"
toaddress =  fromaddress
subject = "I love CS"
contenttype = "text/plain"
username = base64.encodebytes("13072190030".encode()).decode()
passwd = base64.encodebytes("Ai362203".encode()).decode()
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.settimeout(3)
clientSocket.connect(mailserver)
print("connected")
recv = clientSocket.recv(1024)
if recv[:3]!='220':
    print("220 reply not received from server.")

heloCommand = 'HELO 163.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(heloCommand,recv1.decode())
if recv1!='250':
    print("250 reply not received from server.")
# Auth
clientSocket.sendall('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')

clientSocket.sendall((username + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')

clientSocket.sendall((passwd + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '235'):
	print('235 reply not received from server')

mailCommand = 'MAIL FROM: <13072190030@163.com>\r\n'
clientSocket.send(mailCommand.encode())
recv1 = clientSocket.recv(1024)
print(mailCommand,recv1.decode())
if recv1!='250':
    print("250 reply not received from server.")

RcptCommand = 'RCPT TO: <13072190030@163.com>\r\n'
clientSocket.send(RcptCommand.encode())
recv1 = clientSocket.recv(1024)
print(RcptCommand,recv1.decode())
if recv1!='250':
    print("250 reply not received from server.")

dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv1 = clientSocket.recv(1024)
print(dataCommand,recv1.decode())
if recv1!='354':
    print("354 reply not received from server.")

message = 'from:' + fromaddress + '\r\n'
message += 'to:' + toaddress + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-Type:' + contenttype + '\t\n'
message += '\r\n' + msg
clientSocket.sendall(message.encode())
clientSocket.send(endmsg.encode())
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1!='250':
    print("250 reply not received from server.")

endCommand = 'QUIT\r\n'
clientSocket.send(endCommand.encode())
recv1 = clientSocket.recv(1024)
print(endCommand,recv1.decode())
if recv1!='221':
    print("221 reply not received from server.")

