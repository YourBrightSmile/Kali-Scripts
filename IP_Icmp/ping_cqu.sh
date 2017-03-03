#! /bin/bash
if [ "$#" -ne 1 ];then
	echo "Please use ./ping_cqu <interface>"
	exit
fi

interface=$1
prefix=$(ifconfig eth1|grep "netmask"|cut -d "t" -f│2|cut -d " " -f2|cut -d "." -f1-3)
for addr in $(seq 1 254);do
	echo -n -e "/r[$i/254]"
	ping -c 1 $prefix.$i
	
done
echo
