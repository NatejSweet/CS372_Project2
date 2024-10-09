import socket
import sys
import os
from helper_functions import *
port=28333
server_root = os.path.abspath('.')
if len(sys.argv) == 2:
    port = int(sys.argv[1])
s = socket.socket()
#make it reuable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind it to a port
s.bind(('localhost', port))
#listen
s.listen()
print("Listening on port "+str(port))
#loop
while True:
    #accept new connections(new socket)
    c, addr = s.accept()
    header = c.recv(1024)
    header = header.decode()
    requested_file = header.split("\r\n")[0].split(" ")[1]
    if invalid_path(requested_file, server_root): 
        print("Invalid path requested", requested_file, "from", addr)
        c.sendall("HTTP/1.1 403 Forbidden\r\nContent-Type: text/plain\r\nContent-Length: 0\r\nConnection: close\r\n\r\n".encode())
        continue
    else: 
        print("Got connection from", addr, "for", requested_file)
        if (requested_file != "/"):
            data = read_file(requested_file, server_root)
            mime_type = get_mime_type(requested_file)
            if data is not None: #ensure file found
                c.sendall(f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\nContent-Length: {len(data)}\r\nConnection: close\r\n\r\n".encode() + data)
            else:
                c.sendall("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 0\r\nConnection: close\r\n\r\n".encode())
        else:
            #send/recieve data
            mime_type = "text/plain"
            c.sendall("HTTP/1.1 200 OK \r\n Content-Type: {mime_type}\r\n Content-Length: 6 \r\n Connection: close \r\n \r\n Hello!".encode())
    #close the socket
    c.close()
