#!/bin/bash -ex

source config.cfg

#Update for Ubuntu
apt-get -y install ubuntu-cloud-keyring
echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu" \
"trusty-updates/juno main" > /etc/apt/sources.list.d/cloudarchive-juno.list

apt-get update -y && apt-get upgrade -y && apt-get dist-upgrade -y

echo "##### Configuring hostname for COMPUTE1 node... #####"
sleep 3


echo "Cau hinh hostname cho COMPUTE1 NODE"
sleep 3
echo "compute1" > /etc/hostname
hostname -F /etc/hostname

apt-get install ntp -y
apt-get install python-mysqldb -y
#
echo "##### Backup NTP configuration... ##### "
sleep 7 
cp /etc/ntp.conf /etc/ntp.conf.bka
rm /etc/ntp.conf
cat /etc/ntp.conf.bka | grep -v ^# | grep -v ^$ >> /etc/ntp.conf
#
sed -i 's/server 0.ubuntu.pool.ntp.org/ \
#server 0.ubuntu.pool.ntp.org/g' /etc/ntp.conf

sed -i 's/server 1.ubuntu.pool.ntp.org/ \
#server 1.ubuntu.pool.ntp.org/g' /etc/ntp.conf

sed -i 's/server 2.ubuntu.pool.ntp.org/ \
#server 2.ubuntu.pool.ntp.org/g' /etc/ntp.conf

sed -i 's/server 3.ubuntu.pool.ntp.org/ \
#server 3.ubuntu.pool.ntp.org/g' /etc/ntp.conf

sed -i "s/server ntp.ubuntu.com/server $CON_MGNT_IP iburst/g" /etc/ntp.conf


ifaces=/etc/network/interfaces
test -f $ifaces.orig || cp $ifaces $ifaces.orig
rm $ifaces
touch $ifaces
cat << EOF >> $ifaces
#Dat IP cho Controller node

# LOOPBACK NET 
auto lo
iface lo inet loopback

# MGNT NETWORK
auto eth0
iface eth0 inet static
address $COM1_MGNT_IP
netmask $NETMASK_ADD
gateway $GATEWAY_IP
dns-nameservers 8.8.8.8


# VLANs NETWORK
auto eth1
iface eth1 inet manual
up ifconfig \$IFACE 0.0.0.0 up
up ip link set \$IFACE promisc on
down ifconfig \$IFACE 0.0.0.0 down

# VLAN DATA NETWORK
auto eth2
iface eth2 inet manual
up ifconfig \$IFACE 0.0.0.0 up
up ip link set \$IFACE promisc on
down ifconfig \$IFACE 0.0.0.0 down

EOF

#Khoi dong lai cac card mang vua dat
#service networking restart

#service networking restart
# ifdown eth0 && ifup eth0
# ifdown em2 && ifup em2
# ifdown eth2 && ifup eth2

#sleep 5

init 6
#



