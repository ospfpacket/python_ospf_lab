#!/usr/bin/env python3
import sys
sys.path.append('./inventory')
from netmiko import ConnectHandler
from rtr_inv import R1

#Here is the config that is standard among all routers.
net_connect = ConnectHandler(**routers)
config_commands = ['ip domain name ospfpacket']

#Here is the config that is standard among the tunnel routers.
