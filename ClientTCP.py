import socket
import threading

Host='10.0.1.10'#host is host of server NOT CLIENT If not in LAN then use PUBLIC IP only works cause this is LAN
PORT=9990#must be same as python port
Nickname=input("what is your name: ")
Client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((Host,PORT))

def receive():
    while True:
        try:
            message=Client.recv(1024).decode("ascii")
            if message=='G':
                Client.send(Nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("error")
            Client.close()
            break
                
def write():
    while True:
            message='{}:{}'.format(Nickname, input(""))
            Client.send(message.encode('ascii'))
       
       
receive_thread= threading.Thread(target=receive)
receive_thread.start()
write_thread=threading.Thread(target=write)
write_thread.start()
