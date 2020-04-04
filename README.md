Python OSPF Lab
=======

Automate the deployment of a 10 router lab with 5 OSPF areas and connected redistribution

## Quick Links

- [Platforms Used in the Lab](https://github.com/ospfpacket/python_ospf_lab#platforms-used-in-the-lab)
- [Assumptions](https://github.com/ospfpacket/python_ospf_lab#assumptions)
- [Installation](https://github.com/ospfpacket/python_ospf_lab#installation)
- [Common Issues](https://github.com/ospfpacket/python_ospf_lab#installation)

## Platforms Used in the Lab

This lab was run against the following IOL image:
- L3-ADVENTERPRISEK9-M-15.4-2T.bin
- L3-ADVENTERPRISEK9-M-15.2-M5.3.bin

This lab was run with the following python --version

```
Python 3.6.9
```

The following OS was used for this deployment. **Note this was running on the WSL for Windows 10.

```
NAME="Ubuntu"
VERSION="18.04.4 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.4 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

## Assumptions

- Standard connectivity to 10 virtual routers with addresses from 10.0.0.21 - 10.0.0.30
- SSH access to those routers

## Installation

```
Will Update More at a later time.
```

## Common Issues

- Interating through 2 lists at the same time can be done with the zip() function. This essentially uses 2 or more same length lists and runs them through a for loop pairing index 0, 1, 2, etc.
- Inventory File my be in top down order to work through the built out lists.
- WSL and VScode will not like the pathing that is used to verify that the variables have actually been imported. The script works even though VScode errors and says the modules cannot be imported.