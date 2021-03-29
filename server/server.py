import socket
import tqdm
import os
SERVER_HOST = "127.0.0.1" #Host the server at this IP adress
SERVER_PORT = 5001 #Open this port to recieve data.

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()

s.bind((SERVER_HOST, SERVER_PORT))
#if there is 5 unaccepted connections then stop.
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}") #The server listens to this port if the client attempts to access it.

client_socket, address = s.accept()

print(f"[+] {address} is connected.")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR) #Recieve the file test1.txt

filename = os.path.basename(filename)

filesize = int(filesize)

progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024) #File is being recieved
with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read)) #Display a progress bar

client_socket.close()
s.close()