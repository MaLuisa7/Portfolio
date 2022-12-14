import socket

host = 'localhost'
port = 6767

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print('Server listening on port ', port)

s.listen(1)

c , addrs = s.accept()

fileName = c.recv(1024)

try:
    f = open(fileName,'rb')
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    print('Files does not exist')
    c.send(b'Files does not exist')

c.close()
