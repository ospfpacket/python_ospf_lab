Python OSPF Lab
=======

Automate the deployment of a 10 router lab with 5 OSPF areas and connected redistribution

## Quick Links

- [Platforms Used in the Lab](https://github.com/ospfpacket/python_ospf_lab#platforms-used-in-the-lab)
- [Assumptions](https://github.com/ospfpacket/python_ospf_lab#assumptions)
- [Installation](https://github.com/ospfpacket/python_ospf_lab#installation)
- [Common Issues](https://github.com/ospfpacket/python_ospf_lab#installation)

## Platforms Used in the Lab

This lab was run against the following IOL images:
- L3-ADVENTERPRISEK9-M-15.4-2T.bin
- L3-ADVENTERPRISEK9-M-15.2-M5.3.bin

This lab was run with the following python --version

```
Python 3.7.3
```

The following OS was used for this deployment.

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
- Username: user1
- Password: password1
- Enable Secret: secret1

## Installation

```
Will Update More at a later time.
```

## Common Issues

- Interating through 2 lists at the same time can be done with the zip() function. This essentially uses 2 or more same length lists and runs them through a for loop pairing index 0, 1, 2, etc.
- Inventory File my be in top down order to work through the built out lists.
- WSL and VScode will not like the pathing that is used to verify that the variables have actually been imported. The script works even though VScode errors and says the modules cannot be imported. (you can disable pylint in vscode to remove this annoying error)
