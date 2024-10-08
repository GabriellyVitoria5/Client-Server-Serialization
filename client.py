import socket

host = '127.0.0.1'     
port = 5000           
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port)) # destination
socket.send("Hello world!")
socket.close()