#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Arya Tripathi
#
# Created:     03-11-2023
# Copyright:   (c) Arya Tripathi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

server_ip = '192.168.137.11'
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, port))
server.listen(1)

print("Server is listening...")

connection, address = server.accept()
print(f"Connected to {address}")

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print(f"Client: {data}")
    message = input("You: ")
    connection.send(message.encode())

connection.close()
