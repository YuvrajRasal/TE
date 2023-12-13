import socket

def mpm():
    host = '127.0.0.1'
    port = 6000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addr = s.accept()
    print("Address of client is : ",addr)
    while True:
        data = c.recv(1024)
        d = data.decode("ascii")
        print("Message from client : ",d)
        x = input("Enter message : ")
        y = x.encode("ascii")
        c.send(y)
mpm()
    
    