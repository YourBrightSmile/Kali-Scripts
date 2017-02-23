#! /bin/bash
if [ "$#" -ne 1 ];then
	echo "Please Use ./arping_ether.sh <interface>"
	exit
fi

interface=$1
prefix=$(ifconfig $interface|grep 'inet' |head -n 1|cut -d "t" -f2|cut -d" " -f 2|cut -d "." -f1-3)
for((i=1;i<254;i++));do
	echo -n -e "\r[$i/254] "
	arping -c 1 $prefix.$i | grep "bytes from"|cut -d " " -f4-9
	
done

