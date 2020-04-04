#!/usr/bin/env python3
import sys
sys.path.append('../inventory')
from netmiko import ConnectHandler
from rtr_inv import routers, tunnelrouters, tunneloct, loopbacks, hostnames, singleseg, singlesegoct, singleseglastoct, seg146, octet146, seg79, octet79, seg67, octet67, seg37, octet37, seg13, octet13, seg23, octet23, seg45, octet45, seg58, octet58, seg108, octet108

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

#configure interfaces and assign IP addresses
for devicelist, lastoctet in zip(seg79, octet79) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.79',
                       'encap dot 79',
                       'ip address 155.1.79.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()