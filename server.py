import socket
import json

host = '127.0.0.1'  
port = 5000        
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((host, port)) # origin
socket.listen(0) 

print("Server is waiting for connection...")

while True:
    conn, client = socket.accept()
    print ("Connected by", client)

    json_data = conn.recv(1024).decode("utf-8")
    data = json.loads(json_data)
    print(data)

    conn.close()
