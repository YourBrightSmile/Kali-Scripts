#! /bin/bash
if [ "$#" -ne 1 ] && [ "$#" -ne 2 ];then
	echo "Please Use ./arping_ether.sh <interface>  or ./arping_ether <interface> filename"
	exit
fi

getPrefix(){
	inet_first=$(echo $1|cut -d "." -f1)
	inet_second=$(echo $1|cut -d "." -f2)
	inet_third=$(echo $1|cut -d "." -f3)
	inet_fourth=$(echo $1|cut -d "." -f4)
	
	netmk_first=$(echo $2|cut -d "." -f1)
	netmk_second=$(echo $2|cut -d "." -f2)
	netmk_third=$(echo $2|cut -d "." -f3)
	netmk_fourth=$(echo $2|cut -d "." -f4)
		
	pre_first=$((inet_first&netmk_first))
	pre_second=$((inet_second&netmk_second))
	pre_third=$((inet_third&netmk_third))
	pre_fourth=$((inet_fourth&netmk_fourth))
	
	#根据掩码与IP得到网段
	prefix=$pre_first.$pre_second.$pre_third.$pre_fourth
	
	#用掩码得到主机数量
	ip_num1=1
	ip_num2=1
	ip_num3=1
	ip_num4=1	
	if [ "$((netmk_first^255))" -ne 0 ];then
		ip_num1=$(($((netmk_first^255))+1))
	fi
	
	if [ "$((netmk_second^255))" -ne 0 ];then
		ip_num2=$(($((netmk_second^255))+1))
	fi
	
	if [ "$((netmk_third^255))" -ne 0  ];then
		ip_num3=$(($((netmk_third^255))+1))
	fi
	
	if [ "$((netmk_fourth^255))" -ne 0  ];then
		ip_num4=$(($((netmk_fourth^255))+1))	
	fi
	
	ip_num=$((ip_num1*ip_num2*ip_num3*ip_num4))
}

interface=$1
netmask=$(ifconfig eth0|grep 'netmask'|cut -d "t" -f3|cut -d " " -f2)
inet=$(ifconfig $interface|grep 'inet' |head -n 1|cut -d "t" -f2|cut -d" " -f 2|cut -d "." -f1-4)
getPrefix $inet $netmask

if [ "$#" -eq 1 ];then
	if [ $(($ip_num/256/256/256)) -gt 1 ];then
		for((x=0;x<=$(($ip_num/256/256/256));x++));do
			ip1=$(($(echo $prefix|cut -d "." -f1)+$x))
			for((y=1;y<256;y++));do
				ip2=$(($(echo $prefix|cut -d "." -f2)+$y))
				for((z=0;z<256;z++));do
					ip3=$(($(echo $prefix|cut -d "." -f3)+$z))
					for((g=0;g<256;g++));do
						ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
						echo -n -e "\r[$g/$ip_num] "
						arping -c 1 $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 
					done				
				done				
			done		
		done	
		echo
	fi
	if [ $(($ip_num/256/256)) -gt 1 ];then	
		ip1=$(echo $prefix|cut -d "." -f1)
		for((y=0;y<$(($ip_num/256/256));y++));do
			ip2=$(($(echo $prefix|cut -d "." -f2)+$y))
			for((z=0;z<256;z++))do
				ip3=$(($(echo $prefix|cut -d "." -f3)+$z))
				for((g=0;g<256;g++));do
					ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
					echo -n -e "\r[$g/$ip_num] "
					arping -c 1 $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 
				done				
			done				
		done
		echo			
	fi

	if [ $(($ip_num/256)) -gt 1 ];then	
		ip1=$(echo $prefix|cut -d "." -f1)
		ip2=$(echo $prefix|cut -d "." -f2)
		for((z=0;z<$(($ip_num/256));z++));do
			ip3=$(($(echo $prefix|cut -d "." -f3)+$z))
			for((g=0;g<256;g++));do
				ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
				echo -n -e "\r[$g/$ip_num] "
				arping -c 1 $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 
			done				
		done
		echo							
	fi
	if [ $ip_num -gt 1 ];then	
		ip1=$(echo $prefix|cut -d "." -f1)
		ip2=$(echo $prefix|cut -d "." -f2)
		ip3=$(echo $prefix|cut -d "." -f3)
		for((g=0;g<ip_num;g++));do
			ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
			echo -n -e "\r[$g/$ip_num] "
			arping -c 1 $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 
		done	
		echo										
	fi
	
fi

if [ "$#" -eq 2 ];then
	
	if [ $(($ip_num/256)) -gt 1 ];then	
		ip1=$(echo $prefix|cut -d "." -f1)
		ip2=$(echo $prefix|cut -d "." -f2)
		for((z=0;z<$(($ip_num/256));z++));do
			ip3=$(($(echo $prefix|cut -d "." -f3)+$z))
			for((g=0;g<256;g++));do
				ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
				echo -n -e "\r[$g/$ip_num] "
				arping -c 1 -i $interface $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 >> $2 &
			done				
		done
		echo							
	fi
	if [ $ip_num -gt 1 ];then	
		ip1=$(echo $prefix|cut -d "." -f1)
		ip2=$(echo $prefix|cut -d "." -f2)
		ip3=$(echo $prefix|cut -d "." -f3)
		for((g=0;g<ip_num;g++));do
			ip4=$(($(echo $prefix|cut -d "." -f4)+$g))	
			echo -n -e "\r[$g/$ip_num] "
			arping -c 1 $ip1.$ip2.$ip3.$ip4 | grep "bytes from"|cut -d " " -f4-9 >> $2 &
		done	
		echo										
	fi
		
fi




