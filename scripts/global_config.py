#!/usr/bin/env python3
import sys
sys.path.append('./inventory')
from netmiko import ConnectHandler
from rtr_inv import routers, hostnames, loopbacks, tunnelrouters

#Here is the config that is standard among all routers.
for devicelist, names in zip(routers, hostnames) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['hostname ' + names,
                       'banner login ^',
                       'Welcome to the OSPFPacket Lab!',
                       'Happy Learning!!',
                       '^']
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
for devicelist in tunnelrouters :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['crypto isakmp policy 10',
                       'encr aes',
                       'authentication pre-share',
                       'group 5',
                       'hash md5',
                       'crypto isakmp key cisco address 0.0.0.0',
                       'crypto ipsec transform-set ESP_AES_SHA esp-aes esp-sha-hmac',
                       'crypto ipsec profile DMVPN_PROFILE',
                       'set transform-set ESP_AES_SHA']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()