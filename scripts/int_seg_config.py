#!/usr/bin/env python3
import sys
sys.path.append('./inventory')
from netmiko import ConnectHandler
from rtr_inv import *

#configure single segment routers on singlesegments
for devicelist, octets, lastoct in zip(singleseg, singlesegoct, singleseglastoct) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet 0/0.' + lastoct,
                       'encap dot ' + lastoct,
                       'ip add 155.1.' + octets + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()


#configure interfaces and assign IP addresses on segment 146
for devicelist, lastoctet in zip(seg146, octet146) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.146',
                       'encap dot 146',
                       'ip address 155.1.146.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 79
for devicelist, lastoctet in zip(seg79, octet79) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.79',
                       'encap dot 79',
                       'ip address 155.1.79.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 37
for devicelist, lastoctet in zip(seg37, octet37) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.37',
                       'encap dot 37',
                       'ip address 155.1.37.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 67
for devicelist, lastoctet in zip(seg67, octet67) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.67',
                       'encap dot 67',
                       'ip address 155.1.67.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 100
for devicelist, lastoctet in zip(tunnelrouters, tunneloct) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.100',
                       'encap dot 100',
                       'ip address 169.254.100.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 13
for devicelist, lastoctet in zip(seg13, octet13) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.13',
                       'encap dot 13',
                       'ip address 155.1.13.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 23
for devicelist, lastoctet in zip(seg23, octet23) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.23',
                       'encap dot 23',
                       'ip address 155.1.23.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 45
for devicelist, lastoctet in zip(seg45, octet45) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.45',
                       'encap dot 45',
                       'ip address 155.1.45.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 58
for devicelist, lastoctet in zip(seg58, octet58) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.58',
                       'encap dot 58',
                       'ip address 155.1.58.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure interfaces and assign IP addresses on segment 108
for devicelist, lastoctet in zip(seg108, octet108) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface ethernet0/0.108',
                       'encap dot 108',
                       'ip address 155.1.108.' + lastoctet + ' 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configuretunnel interface on spoke routers
for devicelist, lastoctet in zip(tunnelspokes, tunnelspokeoct) :
    net_connect = ConnectHandler(**devicelist)
    net_connect.enable()
    config_commands = ['interface Tunnel0',
                       'ip address 155.1.0.' + lastoctet + ' 255.255.255.0',
                       'ip mut 1400',
                       'ip nhrp authentication NHRPPASS',
                       'ip nhrp map 155.1.0.5 169.254.100.5',
                       'ip nhrp map multicast 169.254.100.5',
                       'ip nhrp network-id 1',
                       'ip nhrp holdtime 300',
                       'ip nhrp nhs 155.1.0.5',
                       'ip tcp adjust-mss 1360',
                       'tunnel source Ethernet0/0.100',
                       'tunnel mode gre multipoint',
                       'tunnel key 150',
                       'tunnel protection ipsec profile DMVPN_PROFILE',
                       'no shutdown']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()

#configure tunnel interface on hub router
net_connect = ConnectHandler(**R5)
net_connect.enable()
config_commands = ['interface Tunnel0',
                   'ip address 155.1.0.5 255.255.255.0',
                   'ip mut 1400',
                   'ip nhrp authentication NHRPPASS',
                   'ip nhrp map multicast dynamic',
                   'ip nhrp network-id 1',
                   'ip tcp adjust-mss 1360',
                   'delay 1000',
                   'tunnel source Ethernet0/0.100',
                   'tunnel mode gre multipoint',
                   'tunnel key 150',
                   'tunnel protection ipsec profile DMVPN_PROFILE',
                   'no shutdown']
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()