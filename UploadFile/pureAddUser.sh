#!/bin/bash
groupadd ftpgroup
useradd -g ftpgroup -d /dev/null -s /etc ftpuser
pure-pw useradd gg -u ftpuser -d /ftpGG
pure-pw mkdb
cd /etc/pure-ftpd/auth/
ln -s ../conf/PureDB 60pdb
mkdir -p /ftpGG
chown -R ftpuser:ftpgroup /ftpGG/
/etc/init.d/pure-ftpd restart
