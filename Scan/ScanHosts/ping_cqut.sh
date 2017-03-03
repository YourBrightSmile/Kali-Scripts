#! /bin/bash
interface=$1
prefix1=$(ifconfig $interface|grep "netmask"|cut -d "t" -f2|cut -d " " -f2|cut -d "." -f1-2)
prefix2=$(ifconfig $interface|grep "netmask"|cut -d "t" -f2|cut -d " " -f2|cut -d "." -f3)
n=1
for ((i=0;i<4;i++));do
	prefix2=$(($prefix2+$i))
	
	for addr in $(seq 1 254);do
		echo -n -e "\r[$((n++))/$((4*254))] "
		
		ping -c 1 $prefix1.$prefix2.$addr|grep "bytes from" &
		
	done
done
echo
