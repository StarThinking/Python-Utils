import socket

s = socket.socket()

host = socket.gethostname()
port = 1242
s.bind(('localhost', port))

s.listen(5)
while True:
    c, addr = s.accept()
    try:
	c.settimeout(5)
        buf = c.recv(1024)  
        print 'Got connection from', addr
        print "Got content" + buf
        c.send("Welcome to server!" +buf)  
    except socket.timeout:
	print 'time out' 
	
    c.close()
