#!/usr/bin/env python3
import sys
sys.path.append('/home/ospfpacket/code/python/ospf_automation_lab/scripts')
import global_config
import int_seg_config
import ospf_config

exec('global_config')
exec('int_seg_config')
exec('ospf_config')
