import socket
import sys

ipadd='127.0.0.5'
p_no =5005
buff_size = 1024*10
soc= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((ipadd,p_no))
soc.listen(1)
conn,addr = soc.accept()
mass =""
uname  = conn.recv(buff_size).decode()
data=b''
while mass != "bye":
    print(data.decode())
    if mass[0:2] == "cd":
        uname = data.decode()
    print(uname,end="")
    mass = input(" >> ",)
    if mass == "exit":
        sys.exit()
    conn.send(mass.encode())
    data  = conn.recv(buff_size)
conn.close()
