import socket

# create socket object
s = socket.socket()

# get local machine name
host = socket.gethostname()

# choose a port number
port = 12345

# bind socket to port
s.bind((host, port))

# listen for incoming connections
s.listen(5)

print('Waiting for connection...')

# accept incoming connection
conn, addr = s.accept()

print(f"Connection established with {addr[0]}:{addr[1]}")


import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print("Selected file:", file_path)

# open file to send
filename = file_path
f = open(filename, 'rb')
l = f.read(1024)

# send file
while l:
    conn.send(l)
    l = f.read(1024)

print('File sent successfully')

# close connection and file
f.close()
conn.close()
