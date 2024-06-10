import socket
import threading

PORT=5050
SERVER=server=socket.gethostbyname(socket.gethostname())    ### IPV4
ADDR=(SERVER,PORT)
HEADER=8
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_clint(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected....")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")
            conn.send("msg received".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread=threading.Thread(handle_clint(conn,addr))    ##(target=handle_clint,args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}")
print("[STARTING] SERVER IS STARTING ........ ")
start()
