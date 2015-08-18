#!/bin/bash -ex

source config.cfg

echo "Cau hinh hostname cho COMPUTE2 NODE"
sleep 3
echo "compute2" > /etc/hostname
hostname -F /etc/hostname


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
auto em1
iface em1 inet static
address $COM2_MGNT_IP
netmask $NETMASK_ADD
gateway $GATEWAY_IP
dns-nameservers 8.8.8.8


# VLANs NETWORK
auto em2
iface em2 inet manual
up ifconfig \$IFACE 0.0.0.0 up
up ip link set \$IFACE promisc on
down ifconfig \$IFACE 0.0.0.0 down

# VLAN DATA NETWORK
auto em3
iface em3 inet manual
up ifconfig \$IFACE 0.0.0.0 up
up ip link set \$IFACE promisc on
down ifconfig \$IFACE 0.0.0.0 down

EOF

#Khoi dong lai cac card mang vua dat
#service networking restart

#service networking restart
# ifdown em1 && ifup em1
# ifdown em2 && ifup em2
# ifdown eth2 && ifup eth2

#sleep 5

init 6
#




