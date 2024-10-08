import socket

host = '127.0.0.1'  
port = 5000        
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((host, port)) # origin
socket.listen(0) 

print("Server is waiting for connection...")

while True:
    conn, client = socket.accept()
    print ("Connected by", client)
    message = conn.recv(1024)
    print ("Client ", client[0], ": ", message)
    conn.close()
