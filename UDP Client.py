import socket

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#SENDING INFO
client.sendto("hello".encode('utf-8'),('255.255.255'))