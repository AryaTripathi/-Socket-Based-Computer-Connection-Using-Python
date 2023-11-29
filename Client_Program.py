import socket
server_ip = '192.168.137.11'
port = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))
while True:
 message = input("You: ")
 client.send(message.encode())
 data = client.recv(1024).decode()
 print(f"Server: {data}")
client.close()