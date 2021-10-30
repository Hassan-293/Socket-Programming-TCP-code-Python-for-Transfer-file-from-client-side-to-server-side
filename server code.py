import socket
import datetime


from socket import socket, AF_INET, SOCK_STREAM
srvaddr = ('127.0.0.1', 11111)

now = datetime.datetime.now()
print("[STARTING] Server is starting.")

server = socket(AF_INET, SOCK_STREAM)
server.bind(srvaddr)
server.listen()

print("[LISTENING] Server is listening.")

while True:
    """ Server has accepted the connection from the client. """
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    """ Receiving the filename from the client. """
    filename = conn.recv(1024).decode("utf-8")
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "w")
    conn.send("Filename received.".encode("utf-8"))

    """ Receiving the file data from the client. """
    print("Here")
    data = conn.recv(1024).decode("utf-8")
    print(f"[RECV] Receiving the file data...")

    print("FILE CONTENT:")
    print(data)
    file.write(data)
    #conn.send("File data received".encode("utf-8"))

    dataa = input("ENTER NEW DATA: ")
    file.write(dataa)
    print("Time: ",now.strftime("%Y-%m-%d %H:%M:%S"))
    file.close()

    file = open(filename, "r")
    getdata = file.read()
    print("UPDATED FILE:")
    print(getdata)
    """ Closing the file. """
    file.close()

    """ Closing the connection from the client. """
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

