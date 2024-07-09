import socket 


target = "127.0.0.1"
target_port = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

with client_socket:
    
    client_socket.connect((target,target_port))
    
    while client_socket:
        msg = input('enter the command that you want to test: ')
        client_socket.send(f"{msg}".encode('utf-8'))
    
        res , addr = client_socket.recvfrom(target_port)
    
        print('>> ',res.decode('utf-8'))
