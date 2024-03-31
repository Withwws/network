import socket

while True:
    line = input("ftp> ").strip()
    args = line.split()
    
    command = args[0]
    if command == "quit":
        break
    elif command == "open":
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(args[1], args[2])