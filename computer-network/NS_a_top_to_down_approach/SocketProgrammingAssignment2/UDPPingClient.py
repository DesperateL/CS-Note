from socket import *
import time

ClientSocket = socket(AF_INET,SOCK_DGRAM)
ClientSocket.settimeout(1)

sumTime = 0
counter = 0
total = 10
for i in range(total):
    startTime = time.time()
    message = "Ping %d %f" %(i,startTime)
    ClientSocket.sendto(message.encode(),("localhost",12000))
    try:
        resp,addr = ClientSocket.recvfrom(1024)
        endTime = time.time()
        sumTime += endTime-startTime
        counter += 1
        print(resp.decode(),"%f"%(endTime-startTime))
    except Exception:
        print("Request time out!")
if sumTime==0.0:
    print("avgRTT:max,lossRate:100%")
else:
    print("avgRTT:%f,lossRate:%f"%(sumTime/counter,(total-counter)/total))    
