import socket
import json

host = '127.0.0.1'     
port = 5000           
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port)) # destination

print("Inform your credentials below:")
name = input("Name: ")
age = input("Age: ")
cpf = input("CPF: ")
message = input("Message: ")

data = {
    "Name": name,
    "CPF": cpf,
    "Age": age,
    "Message": message
}

json_data_serialized = json.dumps(data)
socket.sendall(json_data_serialized.encode("utf-8"))

socket.close()