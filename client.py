import socket
import json
import toml
import yaml
import io
import csv
import dicttoxml

host = '127.0.0.1'     
port = 5000           
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port)) # destination

print("Client", host, "connected to the server on port", port)

print("\nInform your credentials below:")
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

# yaml
yaml_data_serialized = yaml.dump(data)
socket.send(yaml_data_serialized.encode("utf-8"))

# csv 

# convert dictionary to csv
output = io.StringIO()  
writer = csv.DictWriter(output, fieldnames=data.keys())
writer.writeheader()  
writer.writerow(data)  

csv_data_serialized = output.getvalue()
output.close()

socket.send(csv_data_serialized.encode("utf-8"))

# xml
xml_data = dicttoxml.dicttoxml(data).decode()
socket.send(xml_data.encode("utf-8"))

socket.close()