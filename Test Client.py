import socket
Host='255.255.255'#host is host of server NOT CLIENT If not in LAN then use PUBLIC IP only works cause this is LAN
PORT=9090#must be same as python port

socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.connect((Host,PORT))

socket.send("Helloooooo".encode('utf-8'))
