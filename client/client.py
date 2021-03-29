import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes in each step.

host = "127.0.0.1" #Look for this IP Adresss to connect to
port = 5001 #look for port 5001
filename = "test1.txt"
filesize = os.path.getsize(filename)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+} Connected.")

s.send(f"{filename}{SEPARATOR}{filesize}".encode("utf-8")) #Send the file test1.txt

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break #transmission finished
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close