#!/usr/bin/python
#coding=utf-8

import logging		#导入日志模块
import subprocess	#导入系统指令
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) #日志等级的设置
from scapy.all import * #from import语法 导入某个模块的具体内容

#print len(sys.argv)
#print (sys.argv[0])	#sys.argv[0]为执行的命令本身
if len(sys.argv) != 2:
	print "Please Use ./arp.py <interfacee>"
	sys.exit()

interface=str(sys.argv[1])
prefix=subprocess.check_output("ifconfig " +interface+" | grep 'inet' |head -n 1|cut -d  't' -f2|cut -d' ' -f 2|cut -d '.' -f1-3",shell=True).strip()+"."
for addr in range(0,254):
	tip="\r["+str(addr)+"/254]"
	os.system("echo -n -e \'"+tip+"\'")
	answer=sr1(ARP(pdst=prefix+str(addr)),timeout=0.1,verbose=0)
	if answer==None:
		pass
	else:
		print prefix+str(addr)
