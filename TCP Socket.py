import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Defines type of socket AF_INET =internet socket,SOCK_STREAM=TCP protocol#just for accepting connections not to be used to send
Host=socket.getaddrinfo(socket.gethostname(),9090)
print(Host)

server.bind(('10.0.1.10',9090))
server.listen(5)#if more than 5 connections waiting then reject
#ONLY USE COMMUNICATION SOCKET TO TALK TO CLIENT SERVER IS ONLY FOR ACCEPTING CONNECTIONS


while True:
        print("stece")
        (communication_socket, address)=server.accept()#returns address of client which connection and the clients comm socket
        print(f"connected to {address}")
        message=communication_socket.recv(1024).decode('utf-8')#1024 is buffur size
        print(f"message from client is:{message}")
        communication_socket.send(f"Got your message!Thank you!".encode('utf-8'))
        communication_socket.close()
        print(f"Connection with {address}ended!")
 