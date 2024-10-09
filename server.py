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

# Método para imprimir dados deserializados
def print_data_deserialized(data_type, data):
    print(data_type, ":", data)
    #print_data_deserialized("JSON", json_data_deserialized)

def deserialize_csv(conn):
    # convert CSV back to dictionary
    csv_data = receive_data(conn)
    csv_reader = csv.DictReader(io.StringIO(csv_data))  
    return list(csv_reader)[0]  

def deserialize_json(conn):
    json_data = receive_data(conn)
    return json.loads(json_data)

def deserialize_xml(conn):
    xml_data = receive_data(conn)
    root = ET.fromstring(xml_data)
    xml_data_desserialized = {}
    for element in root:
        xml_data_desserialized[element.tag] = element.text
    return xml_data_desserialized

def deserialize_yaml(conn):
    yaml_data = receive_data(conn)
    return yaml.safe_load(yaml_data)

def deserialize_toml(conn):
    toml_data = receive_data(conn)
    return toml.loads(toml_data)

print("Server is waiting for connection...")

while True:
    conn, client = socket.accept()
    print ("Connected by", client)

    print_data_deserialized("JSON",deserialize_json(conn))
    print_data_deserialized("TOML",deserialize_toml(conn))
    print_data_deserialized("YAML",deserialize_yaml(conn))
    print_data_deserialized("CSV",deserialize_csv(conn))
    print_data_deserialized("XML",deserialize_xml(conn))
    
    conn.close()

    