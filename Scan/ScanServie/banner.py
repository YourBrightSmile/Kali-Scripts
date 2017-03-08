#!/usr/bin/python
#encoding=utf-8
import select
import socket
import sys

if len(sys.argv)!=4:
	print "Please Use ./banner.py ip portStart portEnd...."
	sys.exit
ip=str(sys.argv[1])
portS=int(sys.argv[2])
portE=int(sys.argv[3])
for port in range(portS,portE):
	try:			
		banner=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		banner.connect((ip,port))
		ready=select.select([banner],[],[],1)#超时时间为1
		if ready[0]:
			
			print "TCP port:"+str(port)+"\n"+banner.recv(4096)
			banner.close()	
	except:
		pass

