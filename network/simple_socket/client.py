import socket
import time

s = socket.socket()

host = 'localhost'
port = 1242

s.connect((host, port))
s.send('I am Vincent')
print s.recv(1024)

s.close()



