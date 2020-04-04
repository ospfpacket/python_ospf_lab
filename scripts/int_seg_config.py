#!/usr/bin/env python3
import sys
sys.path.append('../inventory')
from netmiko import ConnectHandler
from rtr_inv import seg146, octet146, singleseg, singlesegoct, singleseglastoct

#configure single segment routers
for devicelist, octets, lastoct in zip(singleseg, singlesegoct, singleseglastoct) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet 0/0.' + lastoct,
                       'encap dot ' + lastoct,
                       'ip add 155.1.' + octets + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()


#configure interfaces and assign IP addresses
for devicelist, lastoctet in zip(seg146, octet146) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.146',
                       'encap dot 146',
                       'ip address 155.1.146.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()