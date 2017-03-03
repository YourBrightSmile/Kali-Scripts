#! /usr/bin/python
#encoding=utf-8
import time
import logging		#导入日志模块
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) #日志等级的设置
from scapy.all import * #from import语法 导入某个模块的具体内容

if len(sys.argv) != 4:
	print "Please Use ./scanpy_port.py ip port1 port2 "
	sys.exit()
ip=str(sys.argv[1])
startP=int(sys.argv[2])
endP=int(sys.argv[3])
for port in range(startP,endP):
	a=sr1(IP(dst=ip)/UDP(dport=port),timeout=1,verbose=0)
	if (a==None):
		print port
	else :
		pass
