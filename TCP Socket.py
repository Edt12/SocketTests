import socket
hostipaddress=socket.gethostname()
print(hostipaddress)
Host=socket.gethostbyname(hostipaddress)#change to get host name when outside vm 
PORT=9090
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Defines type of socket AF_INET =internet socket,SOCK_STREAM=TCP protocol#just for accepting connections not to be used to send

server.bind((Host, PORT))
server.listen(5)#if more than 5 connections waiting then reject

while True:
    communication_socket, address=server.accept()#returns address of client which connection and the clients comm socket
    print(f"connected to {address}")
    message=communication_socket.recv(1024).decode('utf-8')#1024 is buffur size
    print(f"message from client is:{message}")
    communication_socket.send(f"Got your message!Thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address}ended!")