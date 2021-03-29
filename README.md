# Overview

This program was a networking one meant to move a file from the client to the server using python as the basis.

This program would take the file test1.txt from the client and send it to the server to recieve.

I created this program to have a first time experience on networking with python.

[Software Demo Video](https://youtu.be/LE7Z-Vm8B2Y)

## Network Communication

I used a client and server connection using TCP with the IP Address 127.0.0.1 and port number 5001

The server will listen open and listen to the port number for any data being recieved the client will send send the file and the server will recieve it showing a progress bar and the speed of which the file was sent.

## Development Environment

* Visual Studio Code
* Command Prompt
* Python 3.9.2 64-Bit
* Libraries Socket, tqdm, and OS

## Useful Websites

* [Tutorials Point](https://www.tutorialspoint.com/python/python_networking.htm)
* [Real Python](https://realpython.com/python-sockets/)
* [Python Server Libraries](https://docs.python.org/3.6/library/socketserver.html)
* [Python Socket Libraries](https://docs.python.org/3.6/library/socket.html)

## Future Work

* Try to move multiple files at once
* Try to move files of different types such as img, png, or mp4
