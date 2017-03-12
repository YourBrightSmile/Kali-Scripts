#!/usr/bin/python
import sys
from scapy.all import *
	
if len(sys.argv)!=3:
	print "Pleas use ./scan_fw.py 1.1.1.1 port"
	sys.exit()

ip=str(sys.argv[1])
port=int(sys.argv[2])

syn_resp=sr1(IP(dst=ip)/TCP(dport=port,flags="S"),timeout=1,verbose=0)
ack_resp=sr1(IP(dst=ip)/TCP(dport=port,flags="A"),timeout=1,verbose=0)

if syn_resp==None and ack_resp==None:
	print "port is closed or host is down "
elif ((int(syn_resp[TCP].flags)==18  or int(syn_resp[TCP].flags)==6) and ack_resp==None) or (syn_resp==None and int(ack_resp[TCP].flags)==4 ):
	print "port is filtered"
elif (int(syn_resp[TCP].flags)==18 or int(syn_resp[TCP].flags)==6) and int(ack_resp[TCP].flags)==4:
	print "port is unfiltered and open"
elif int(syn_resp[TCP].flags)==20:
	print "port is unfiltered and closed"
else:
	print "Unable to determine"
