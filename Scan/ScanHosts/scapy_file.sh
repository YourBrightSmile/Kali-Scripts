#! /usr/bin/python
#encoding=utf-8
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv)!=2:
	print "Please User ./scapy_file.sh filename"
	sys.exit();
filename=str(sys.argv[1])
file=open(filename,'r') #打开文件
for addr in file:
	a=sr1(IP(dst=addr.strip())/ICMP(),timeout=0.1,verbose=0)
	if a==None:
		pass
	else:
		print addr.strip()



