import customtkinter as ctk
import sqlite3
import  hashlib
import os
import socket
import multiprocessing
conn=sqlite3.connect("Teams+/Database.db")
cursor=conn.cursor()

#defining screen height and width
ScreenHeightStarting=800
ScreenWidthStarting=800
DirectoryPath=os.path.dirname(os.path.abspath(__file__))#gets directory path of the file

def SocketClient():#creating tcp socket so can receive messages
  
    Host=''#host is host of server NOT CLIENT If not in LAN then use PUBLIC IP only works cause this is LAN
    PORT=9090#must be same as python port

    Client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Client.connect((Host,PORT))

    Client.send("Helloooooo".encode('ascii'))
    Client.listen()
    if Client.recv=="GIB NICKNAME".encode("ascii"):
        print("steve")
        Client.send("Dave".encode("ascii"))
        
def GUI():
    class MainWindow(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.geometry(str((ScreenWidthStarting))+"x"+str((ScreenHeightStarting)))
            self.title("MessageApp")
            def Login():
                Username=UsernameEntry.get()
                Password=PasswordEntry.get()#grabs inputs from username and password boxes encodes then hashes them to compare to entry in database
    
                EncodedUsername=Username.encode('utf-8')
                EncodedPassword=Password.encode('utf-8')
                
                HashedUsername=hashlib.sha3_512(EncodedUsername)
                HashedPassword=hashlib.sha3_512(EncodedPassword)
                
                cursor.execute("Select*from UsernamesAndPasswords")
                UsersAndPasswords=cursor.fetchall()
                print(UsersAndPasswords)
                for row in UsersAndPasswords:
        
                    if row[0]==HashedUsername.hexdigest() and row[1]== HashedPassword.hexdigest():
                        print("correct")
                        LoginFrame.destroy()
                        MessageFrame.place(relheight=1,relwidth=1)
            #creating Login Frame                
            LoginFrame=ctk.CTkFrame(self)
            LoginFrame.place(relheight=1,relwidth=1)#Frame which contains all widgets for the login screen
            Button=ctk.CTkButton(LoginFrame,
                                text="Enter",
                                hover_color="blue",
                                command=Login)
            
            Button.place(relheight=0.05,relwidth=0.1,relx=0.6,rely=0.4)
            UsernameEntry=ctk.CTkEntry(LoginFrame,placeholder_text="Username")
            UsernameEntry.place(relheight=0.05,relwidth=0.15,relx=0.4,rely=0.4)
            PasswordEntry=ctk.CTkEntry(LoginFrame,placeholder_text="Password")
            PasswordEntry.place(relheight=0.05,relwidth=0.15,relx=0.4,rely=0.5)
            Title=ctk.CTkLabel(LoginFrame,text="Teams+",text_color="White",font=('Bold',20))
            Title.place(relheight=0.1,relwidth=0.2,relx=0.4,rely=0.3)
            #Creating Message Frame
            MessageFrame=ctk.CTkFrame(self)
            label=ctk.CTkLabel(MessageFrame,text="Working")
            label.pack()


    cursor.execute("""Create Table if not exists UsernamesAndPasswords
        (Username blob(512) Primary Key
        ,Password blob(512)
        )""")


    Main=MainWindow()
    Main.mainloop()

GUIThread=multiprocessing.Process(target=GUI)
GUIThread.start()
SocketThread=multiprocessing.Process(target=SocketClient)
SocketThread.start()