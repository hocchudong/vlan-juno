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
    uuid = execute("nova list | grep %s | awk '{print $2}'" %vmname)
    xml_conf = execute("grep -Rin %s /etc/libvirt/qemu" %uuid).split(':')[0]
    tap = execute("cat %s | grep tap | awk '{print $2}'" %xml_conf).split("'")[1]
    return tap

def get_ovs_port(tap):
    port = 'qvo' + tap.split('tap')[1]
    return port

def ctl_traffic(port, rate, burst=1000):
    execute("ovs-vsctl set Interface %s ingress_policing_rate=%s" %(port, rate))
    execute("ovs-vsctl set Interface %s ingress_policing_burst=%s" %(port, burst))


print "Danh sach cac may ao tren Compute: \n", get_list_vm()

vm = raw_input("Ten may ao muon dieu chinh bang thong: ")

a = get_tap(vm)

b = get_ovs_port(a)

rate = raw_input("Bop bang thong cua may ao (bps): ")

ctl_traffic(b, rate)

print 'Success! '
