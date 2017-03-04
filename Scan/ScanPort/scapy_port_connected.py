#! /usr/bin/python
#encoding=utf-8
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
import os
import commands
import time
#TCP 全连接扫描
if len(sys.argv)!=4:
	print "Please Use ./scapy_port_connected.py ip port1 port2"
print "-- set iptables --"
ip=str(sys.argv[1])
(status,output)=commands.getstatusoutput('iptables -L |grep '+'\" '+ip+' \"'+'|grep DROP|grep RST')
commd=str('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d '+ip+' -j DROP')
if output=='':
	os.system(commd)
	print "rules add success"
else:
	print "rules had added"
startP=int(sys.argv[2])
endP=int(sys.argv[3])
for port in range(startP,endP):
	response1=sr1(IP(dst=ip)/TCP(dport=port,flags="S"),timeout=1,verbose=0)
	if response1!=None:
		if response1[TCP].flags==18:
			response2=sr1(IP(dst=ip)/TCP(dport=port,flags="A",ack=response1[TCP].seq+1),timeout=1,verbose=0)
			if response2[TCP].flags==16:
				print port
		else:
			pass
	else:
		pass
