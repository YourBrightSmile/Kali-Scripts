#! /usr/bin/python
#encoding=utf-8
import time
import sys
import logging		#导入日志模块
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) #日志等级的设置
from scapy.all import * #from import语法 导入某个模块的具体内容

if len(sys.argv) != 5:
	print "Please Use ./scapy_port.py ip udp/tcp port1 port2 "
	sys.exit()
ip=str(sys.argv[1])
protocol=str(sys.argv[2]).lower()
startP=int(sys.argv[3])
endP=int(sys.argv[4])
if protocol=="udp":
	for port in range(startP,endP):
		a=sr1(IP(dst=ip)/UDP(dport=port),timeout=1,verbose=0)
		time.sleep(1)
		if a==None:
			print port
		else :
			pass
elif protocol=="tcp":
	for port in range(startP,endP):
		a=sr1(IP(dst=ip)/TCP(dport=port,flags="S"),timeout=1,verbose=0)
		time.sleep(1)
		if a==None:
			pass
		else:
			if int(a[TCP].flags)==18:
				print port
			else:
				pass
else:
	print "Maby Input Wrong"
