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

def serialize_csv(data):
    # convert dictionary to csv
    output = io.StringIO()  
    writer = csv.DictWriter(output, fieldnames=data.keys())
    writer.writeheader()  
    writer.writerow(data)  

    csv_data_serialized = output.getvalue()
    output.close()

    return csv_data_serialized

def serialize_json(data):
    return json.dumps(data)

def serialize_xml(data):
    return dicttoxml.dicttoxml(data).decode()

def serialize_yaml(data):
    return yaml.dump(data)

def serialize_toml(data):
    return toml.dumps(data)

def send_message(serialized_format):
    socket.send(serialized_format.encode("utf-8"))

send_message(serialize_json(data))
send_message(serialize_toml(data))
send_message(serialize_yaml(data))
send_message(serialize_csv(data))
send_message(serialize_xml(data))

socket.close()