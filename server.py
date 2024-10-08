import socket
import json
import toml
import yaml
import io
import csv
import xmltodict
import xml.etree.ElementTree as ET

host = '127.0.0.1'  
port = 5000        
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
socket.bind((host, port)) # origin
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
    toml_data_deserialized = toml.loads(toml_data)
    print(toml_data_deserialized)

    # yaml
    yaml_data = conn.recv(1024).decode("utf-8")
    yaml_data_deserialized =  yaml.safe_load(yaml_data)
    print(yaml_data_deserialized)

    # csv
    csv_data = conn.recv(1024).decode("utf-8")
    csv_reader = csv.DictReader(io.StringIO(csv_data))  
    csv_data_desserialized = list(csv_reader)[0] # convert csv back to dictionary 
    print(csv_data_desserialized)

    # xml
    xml_data = conn.recv(1024).decode("utf-8")

    # convert xml back to dictionary 
    root = ET.fromstring(xml_data)
    xml_data_desserialized = {}
    for element in root:
        xml_data_desserialized[element.tag] = element.text
    
    print(xml_data_desserialized)
    
    conn.close()

    