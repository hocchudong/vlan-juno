#! /usr/bin/python
import sys
import subprocess

def print_format(string):
    print "+%s+" %("-" * len(string))
    print "|%s|" % string
    print "+%s+" %("-" * len(string))

def execute(command, display=False):
    print_format("Executing  :  %s " % command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if display:
        while True:
            nextline = process.stdout.readline()
            if nextline == '' and process.poll() != None:
                break
            sys.stdout.write(nextline)
            sys.stdout.flush()

        output, stderr = process.communicate()
        exitCode = process.returncode
    else:
        output, stderr = process.communicate()
        exitCode = process.returncode

    if (exitCode == 0):
        return output.strip()
    else:
        print "Error", stderr
        print "Failed to execute command %s" % command
        print exitCode, output
        raise Exception(output)

def get_list_vm():
    vm = execute('nova list', True)
    return vm

def get_tap(vmname):
    try:
        uuid = execute("nova list | grep %s | awk '{print $2}'" %vmname)
        xml_conf = execute("grep -Rin %s /etc/libvirt/qemu" %uuid).split(':')[0]
        tap = execute("cat %s | grep tap | awk '{print $2}'" %xml_conf).split("'")[1]
        return tap
    except Exception, e:
        print "VM %s khong nam tren node Compute nay" %vmname, e

def get_qvb_port(tap):
    qvb = 'qvb' + tap.split('tap')[1]
    return qvb
        
def get_ovs_port(tap):
    qvo = 'qvo' + tap.split('tap')[1]
    return qvo

def config_mtu(tap, qvb, qvo, mtu=9000):
    try:
        execute("ip link set mtu %s dev %s" %(mtu, tap))
        execute("ip link set mtu %s dev %s" %(mtu, qvb))
        execute("ip link set mtu %s dev %s" %(mtu, qvo))
        
        # Sua em3 thanh ten card mang ket noi voi may chu vat ly CSDL Oracle
        execute("ip link set mtu %s dev phy-br-em3" %mtu)
        execute("ip link set mtu %s int-br-em3" %mtu)
        execute("ip link set mtu %s dev em3" %mtu)

    except Exception,e:
        print "Co loi khi dat MTU \n", e

def main():
    print "Danh sach cac may ao tren Compute: \n", get_list_vm()
    vm = raw_input("Ten may ao muon dieu chinh MTU: ")
    mtu = raw_input("MTU moi: ")

    tap = get_tap(vm)
    qvb = get_qvb_port(tap)
    qvo = get_ovs_port(tap)

    try:
        config_mtu(tap, qvb, qvo, mtu)
        print "Setup Successful"
    except:
        print "Something go wrong!\n Try again!!!!"
        

main()
