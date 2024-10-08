import socket
import json
import toml

host = '127.0.0.1'  
port = 5000        
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((host, port)) # origem
socket.listen(0) 

print("Server is waiting for connection...")

while True:
    conn, client = socket.accept()
    print ("Connected by", client)

    # json
    json_data = conn.recv(1024).decode("utf-8")
    json_data_deserialized = json.loads(json_data)
    print(json_data_deserialized)

    # toml
    toml_data = conn.recv(1024).decode("utf-8")
    toml_data_deserialized = json.loads(json_data)
    print(toml_data_deserialized)

    conn.close()
