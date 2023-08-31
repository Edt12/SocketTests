import socket
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Defines type of socket AF_INET =internet socket,SOCK_STREAM=TCP protocol#just for accepting connections not to be used to send
Host=socket.getaddrinfo(socket.gethostname(),9090)
print(Host)

server.bind(('10.0.1.10',9090))
server.listen(5)#if more than 5 connections waiting then reject
#ONLY USE COMMUNICATION SOCKET TO TALK TO CLIENT SERVER IS ONLY FOR ACCEPTING CONNECTIONS

Clients=[]
Nicknames=[]

def SendToAll(message):#goes through all clients and sends them what server recieves so can see other peoples messages
    for Client in Clients:
        Client.send(message)
        
def ReceiveFromClient(Client):#run everytime a client connects to server
   while True: 
        try:#basically means doesnt stop when encounters an error
            message=Client.recv(1024)
            SendToAll(message)
        except:#when it does encounter an error does this
            index=Clients.index(Client)#gets index of client then removes it from client list 
            Clients.remove(Client)
            Nickname=Nicknames[index]#does same with nicknames and sends message to other clients saying person has left
            SendToAll('{} left!'.format(Nickname).encode('ascii'))
            Nicknames.remove(Nickname)
            break
def Listen():
    while True:
        #accepts connection with client 
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        
        client.send('GIB NICKNAME'.encode('ascii'))#sends message to client to transmit nickname to server
        Nickname = client.recv(1024).decode('ascii')
        Nicknames.append(Nickname)
        Clients.append(Client)
        
        print("Nickname is {}",format(Nickname))
        SendToAll("{} joined!",format(Nickname).encode('ascii'))
        Client.send('Connected to Server!!!'.encode('ascii'))
        
        thread=threading.Thread(target=ReceiveFromClient)
        thread.start()
        
