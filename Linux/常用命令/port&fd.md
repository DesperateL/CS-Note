#  端口与文件描述符相关

## lsof :列出进程打开的文件描述符
- lsof -p <PID> :列出指定进程打开的文件描述符
- lsof -i:<8080> :查看指定端口8080占用情况（一并查出哪个进程占用）。
## netstat: 查看网络状况
- netstat -ntulp TCP |grep <port> : 查看端口占用情况