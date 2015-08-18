cd /var/lib/libvirt/images/
qemu-img convert -c u14.img -O qcow2 uductest.qcow2
scp uductest.qcow2 uvdc@172.16.69.31:/home/uvdc


glance image-create --name "u14duc" --disk-format qcow2 --container-format bare --is-public True --progress < uductest.qcow2


  <os>
    <type arch='x86_64' machine='pc-i440fx-trusty'>hvm</type>
    <boot dev='cdrom'/>
    <boot dev='hd'/>
    <smbios mode='sysinfo'/>
  </os>

    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='/root/ubuntu-12.04.4-server-amd64.iso'/>
      <target dev='hdc' bus='ide'/>
      <readonly/>
      <address type='drive' controller='0' bus='1' target='0' unit='0'/>
    </disk>


Question 5
What does the following statement do?

x = x + 2

This would fail as it is a syntax error
Increase the speed of the program by a factor of 2
Retrieve the current value for x, add two to it and put the sum back into x
Produce the value "false" because "x" can never equal "x+2"



Question 6
Which of the following elements of a mathematical expression in Python is evaluated first?
Multiplication *
Parenthesis ( )
Subtraction -
Addition +


Question 3
Which of the following variables is the "most mnemonic"?
variable_173
x1q3z9ocd
x
hours

Question 4
def info(name, *infos, **dict):
    print name
    print infos
    print dict
        
info('ducnc', 2,3,4, {'duc':1, 'nam':2})

What gets printed?

Question 
def info(name, **dict, *infos):
    print name
    print infos
    print dict
        
info('ducnc', **{'duc':1, 'nam':2}, 2 , 3, 4)

SyntaxError: invalid syntax

