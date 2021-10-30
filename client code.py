import socket

from socket import socket, AF_INET, SOCK_STREAM
srvaddr = ('127.0.0.1', 11111)


""" Staring a TCP socket. """
client = socket(AF_INET, SOCK_STREAM)
client.connect(srvaddr)

""" Opening and reading the file data. """
file = open("data/yt.txt", "r")
data = file.read()

""" Sending the filename to the server. """
client.send("yt.txt".encode("utf-8"))
msg = client.recv(1024).decode("utf-8")
print(f"[SERVERR]: {msg}")

""" Sending the file data to the server. """
client.send(data.encode("utf-8"))
#msg = client.recv(1024).decode("utf-8")
#print(f"[SERVER]: {msg}")

""" Closing the file. """
file.close()

""" Closing the connection from the server. """
client.close()


