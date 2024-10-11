import socket
import json
import toml
import yaml
import io
import csv
import xml.etree.ElementTree as ET

host = '127.0.0.1'  
port = 5000        
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((host, port)) # origin
socket.listen(0) 

def receive_data(conn):
    return conn.recv(1024).decode("utf-8")

def deserialize_csv(conn):
   
    csv_data = receive_data(conn)

    with open("csv_data.csv", 'w') as file:
        file.write(csv_data)

    # convert CSV back to dictionary
    csv_reader = csv.DictReader(io.StringIO(csv_data))  
    list(csv_reader)[0]  
    print(list(csv_reader)[0])

def deserialize_json(conn):
    json_data = receive_data(conn)

    with open("json_data.json", 'w') as file:
        file.write(json_data)

    print(json.loads(json_data))

def deserialize_xml(conn):
    xml_data = receive_data(conn)
    root = ET.fromstring(xml_data)
    xml_data_desserialized = {}
    for element in root:
        xml_data_desserialized[element.tag] = element.text

    with open("xml_data.xml", 'w') as file:
        file.write(xml_data)

    print(xml_data_desserialized)

def deserialize_yaml(conn):
    yaml_data = receive_data(conn)

    with open("yaml_data.yaml", 'w') as file:
        file.write(yaml_data)

    print(yaml.safe_load(yaml_data))

def deserialize_toml(conn):
    toml_data = receive_data(conn)

    with open("toml_data.toml", 'w') as file:
        file.write(toml_data)

    print(toml.loads(toml_data))

print("Server is waiting for connection...")

while True:
    conn, client = socket.accept()
    print ("Connected by", client)

    # json
    json_data = receive_data(conn)
    print(json.loads(json_data))

    # toml
    toml_data = receive_data(conn)
    print(toml.loads(toml_data))

    # yaml
    yaml_data = receive_data(conn)
    print(yaml.safe_load(yaml_data))

    # csv
    csv_data = receive_data(conn)
    # convert CSV back to dictionary
    csv_reader = csv.DictReader(io.StringIO(csv_data))  
    print(list(csv_reader)[0])  

    # xml
    xml_data = receive_data(conn)
    root = ET.fromstring(xml_data)
    xml_data_desserialized = {}
    for element in root:
        xml_data_desserialized[element.tag] = element.text

    print(xml_data_desserialized)


    with open("json_data.json", 'w') as file:
        file.write(json_data)

    with open("toml_data.toml", 'w') as file:
        file.write(toml_data)

    with open("yaml_data.yaml", 'w') as file:
        file.write(yaml_data)

    with open("csv_data.csv", 'w') as file:
        file.write(csv_data)

    with open("xml_data.xml", 'w') as file:
        file.write(xml_data)

    #deserialize_json(conn)
    #deserialize_toml(conn)
    #deserialize_yaml(conn)
    #deserialize_csv(conn)
    #deserialize_xml(conn)
    
    conn.close()

    