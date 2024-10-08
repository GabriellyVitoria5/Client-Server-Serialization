import socket
import json
import toml

host = '127.0.0.1'     
port = 5000           
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port)) # destino

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

# json
json_data_serialized = json.dumps(data)
socket.send(json_data_serialized.encode("utf-8"))

# toml
toml_data_serialized = toml.dumps(data)
socket.send(toml_data_serialized.encode("utf-8"))

socket.close()