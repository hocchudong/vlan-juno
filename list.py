# SSH vào từng node và thực hiện các công việc sau:
# Cài đặt IP cho tất cả các card mạng (nếu có thể hãy đặt giống như mô hình xây dựng hệ thống)
# Nếu muốn cài đặt nhanh thì có thể sử dụng lệnh dhclient để cấp dhcp cho card mạng. Ví dụ 'dhclient eth0'
# Sử dụng lệnh landscape-sysinfo để kiểm tra IP của các card mạng. Với node Controller cần 2 card, Network và Compute mỗi node cần 3 card

# Trên các minion

# Cai dat salt minion
apt-get update
apt-get install python-software-properties -y
add-apt-repository ppa:saltstack/salt -y
apt-get update
apt-get install salt-minion -y

# Cấu hình minion trỏ về IP của master
vi /etc/salt/minion
master: 172.16.69.246

# Cấu hình id của các minion, với mỗi node controller, network, compute đặt id tương tự
vi /etc/salt/minion_id
controller

# Restart salt-minion
service salt-minion restart


# Trên Master

# Thực thi cài đặt IP cho các minion theo mô hình
salt '*' state.sls ipconfig

# Sau khi thực hiện câu lệnh trên thì cả 3 máy chủ sẽ tự động restart. Kết quả trả về sẽ như hình dưới.
# Thực hiện lệnh sau để test xem các minion đã kết nối lại hay chưa.
salt '*' test.ping

# Thực hiện việc cài đặt OPS
salt '*' state.highstate

# Reboot các máy chủ
salt '*' cmd.run reboot
