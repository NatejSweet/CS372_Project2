import socket
import sys

if len(sys.argv) < 2:
    print("Usage: python webclient.py <host> <port(optional)> <file_path(optional)>")
    sys.exit(1)

host = sys.argv[1]
port = sys.argv[2] if len(sys.argv) > 3 else 80
file_path = sys.argv[3] if len(sys.argv) == 4 else "/"

s = socket.socket()
s.connect((host, int(port)))

request = f"GET {file_path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
s.sendall(request.encode('utf-8'))

d = s.recv(4096)
if len(d) == 0:
    print("No data received")
else:
    decoded = d.decode("utf-8")
    print(decoded)

s.close()
