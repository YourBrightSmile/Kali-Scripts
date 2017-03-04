#! /usr/bin/python
#encoding=utf-8
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#### ZOMBIE SCAN
def SCAN(zombie,target,portS,portE):
	print "---------Ports Opened---------"		
	for port in range(portS,portE):
		try:		
			r1=sr1(IP(dst=zombie)/TCP(flags="SA",dport=port),timeout=1,verbose=0)
			send=sr1(IP(src=zombie,dst=target)/TCP(flags="S",dport=port),verbose=0)
			r2=sr1(IP(dst=zombie)/TCP(flags="SA",dport=port),timeout=1,verbose=0)
			if (r1[IP].id+2)==r2[IP].id:	
				print "  ",port	
		except:	
			pass
#IPID TEST
def IPID(zombie):
	"""
	sr1与send的区别 
		sr1发送并接收一个包
		send只发送不接受
	"""
	r1=sr1(IP(dst=zombie)/TCP(flags="SA"),timeout=2,verbose=0)
	send(IP(dst=zombie)/TCP(flags="SA"),verbose=0)
	r2=sr1(IP(dst=zombie)/TCP(flags="SA"),timeout=2,verbose=0)
	if r1==None or r2==None:
		print "The ip seems can not use ,it's not increamental or idle"
	elif r2[IP].id == (r1[IP].id+2):
		print "The zombie ip seems can use. "
		ans=raw_input("Do you want to use this zombie to scan target? Y/N")
		if ans=="Y"or ans== "y" or ans=="":
			target=raw_input("Enter the ip address of target:")
			port1=int(raw_input("Enter the begin port:"))
			port2=int(raw_input("Enter the end port:"))
			SCAN(zombie,target,port1,port2) 
		else:
			sys.exit
		
print "-----------------------ZOMBIE SCAN-----------------------"
print "		1.TEST IPID"
print "		2.START ZOMBIE SCAN WITH KNOWN IP ADDRESS"
print "		3.QUIT"
opt=raw_input("Please Choose:")
if opt=="1":
	zombie=raw_input("Which ip do you want to test:")
	IPID(zombie)
elif opt=="2":
	zombie=raw_input("Which zombie ip do you want to use:")
	target=raw_input("Enter the ip address of target:")
	port1=int(raw_input("Enter the begin port:"))
	port2=int(raw_input("Enter the end port:"))
	SCAN(zombie,target,port1,port2)
elif opt=="3":
	sys.exit

