import socket




server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('10.0.1.10',9999))


#dont listen for connections as udp is connectionless protocol
message,address=server.recvfrom(1024)
print(message.decode('utf-8'))