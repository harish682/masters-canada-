import socket

# create socket object
s = socket.socket()

# get local machine name
host = socket.gethostname()

# choose a port number
port = 12345

# connect to sender
s.connect((host, port))

print('Connected to sender')

# receive file
filename = 'received_file.txt'
with open(filename, 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

print('File received successfully')

# close connection
s.close()
