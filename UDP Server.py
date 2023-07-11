import socket



hostipaddress=socket.gethostname()
server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((hostipaddress,9999))
server.bind()

#dont listen for connections as udp is connectionless protocol
message,address=server.recvfrom(1024)
print(message.decode('utf-8'))