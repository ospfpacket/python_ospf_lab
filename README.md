Python OSPF Lab
=======

Automate the deployment of a 10 router lab with 5 OSPF areas and connected redistribution

## Quick Links

- [Platforms Used in the Lab](https://github.com/ospfpacket/ansible-ospf-lab#platforms-used-in-the-lab)
- [Assumptions](https://github.com/ospfpacket/ansible-ospf-lab#assumptions)
- [Installation](https://github.com/ospfpacket/ansible-ospf-lab#installation)
- [Common Issues](https://github.com/ospfpacket/ansible-ospf-lab#common-issues)

## Platforms Used in the Lab

This lab was run against the following IOL image:
- L3-ADVENTERPRISEK9-M-15.4-2T.bin
- L3-ADVENTERPRISEK9-M-15.2-M5.3.bin

This lab was run with the following ansible --version and python --version

```
ansible 2.7.7
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/pi/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.7.3 (default, Dec 20 2019, 18:57:59) [GCC 8.3.0]
```

The following linux platform used to host Ansible from a raspberry-pi

```
PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
NAME="Raspbian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
```

## Assumptions

- Standard connectivity to 10 virtual routers with addresses from 10.0.0.21 - 10.0.0.30
- SSH access to those routers
- username with privilege level 15 as there is no 'become' or 'become_method' used in this script

## Installation

## Common Issues

Using some of the newer Ansible features that were used in 2.9 are not available with the IOL images. Please make sure to use an Ansible version older than 2.9 so you do not run into a situation where the network modules are not deprecated.
