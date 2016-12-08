import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket Created"
port = 9220
ip = "192.168.223.1"

s.connect ((ip, port))
print "Socket Connected to HOST on ip "+ ip

reply = ''
while True:
    message = "OPEN\r\n"
    reply += s.recv(1024)
    if not reply:
        break
    break
    if '220 HP GGW server (version 1.0) ready' in reply:
        s.sendall(message)
        break    
#reply += s.recv(65535)
print reply
