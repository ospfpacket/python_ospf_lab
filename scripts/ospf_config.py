#!/usr/bin/env python3
import sys
sys.path.append('./inventory')
from netmiko import ConnectHandler
from rtr_inv import *

#configure global ospf settings on all routers
for devicelist, ips in zip(routers, loopbacks) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['router ospf 1',
                       'router-id ' + ips,
                       'redistribute connected']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#Configure Tunnel0 for Area 0 on all tunnel routers
for devicelist in tunnelrouters :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface Tunnel0',
                       'ip ospf 1 area 0',
                       'ip ospf network point-to-multipoint']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 146
for devicelist in seg146 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.146',
                       'ip ospf 1 area 1']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 79
for devicelist in seg79 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.79',
                       'ip ospf 1 area 2']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 37
for devicelist in seg37 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.37',
                       'ip ospf 1 area 2']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 67
for devicelist in seg67 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.67',
                       'ip ospf 1 area 2']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 13
for devicelist in seg13 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.13',
                       'ip ospf 1 area 4']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 23
for devicelist in seg23 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.23',
                       'ip ospf 1 area 5']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 45
for devicelist in seg45 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.45',
                       'ip ospf 1 area 0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 58
for devicelist in seg58 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.58',
                       'ip ospf 1 area 3']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 108
for devicelist in seg108 :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.108',
                       'ip ospf 1 area 3']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#Config R9 Seg9 for Area 2
net_connect = ConnectHandler(**R9)
net_connect.enable()
config_commands = ['interface ethernet0/0.9',
                   'ip ospf 1 area 2']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()

#Config R7 Seg7 for Area 2
net_connect = ConnectHandler(**R7)
net_connect.enable()
config_commands = ['interface ethernet0/0.7',
                   'ip ospf 1 area 2']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()

#Config R5 Seg5 for Area 3
net_connect = ConnectHandler(**R5)
net_connect.enable()
config_commands = ['interface ethernet0/0.5',
                   'ip ospf 1 area 3']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()

#Config R8 Seg8 for Area 3
net_connect = ConnectHandler(**R8)
net_connect.enable()
config_commands = ['interface ethernet0/0.8',
                   'ip ospf 1 area 3']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()

#Config R10 Seg10 for Area 3
net_connect = ConnectHandler(**R10)
net_connect.enable()
config_commands = ['interface ethernet0/0.10',
                   'ip ospf 1 area 3']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()