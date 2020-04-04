#!/usr/bin/env python3
import sys
sys.path.append('./inventory')
from netmiko import ConnectHandler
from rtr_inv import loopbacks, hostnames, routers

#Here is the config that is standard among all routers.
for devicelist, names in zip(routers, hostnames) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['hostname ' + names]
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

for devicelist, ips in zip(routers, loopbacks) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['int loop0',
                     'ip address ' + ips + ' 255.255.255.0',
                     'descr Created with Python and Netmiko!!']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()


#Here is the config that is standard among the tunnel routers.
