import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1337))
while 1:
    dataFromClient = s.recv(1024)
    print(dataFromClient)
