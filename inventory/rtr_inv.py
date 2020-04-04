R1 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.21',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R2 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.22',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R3 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.23',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R4 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.24',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R5 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.25',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R6 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.26',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R7 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.27',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R8 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.28',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R9 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.29',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

R10 = {
    'device_type': 'cisco_ios',
    'host': '10.0.0.30',
    'username': 'user1',
    'password': 'password1',
    'secret': 'secret1'
}

routers = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10]
tunnelrouters = [R1, R2, R3, R4, R5]
tunneloct = ['1', '2', '3', '4', '5']
tunnelspokes = [R1, R2, R3, R4]
tunnelspokeoct = ['1', '2', '3', '4']
loopbacks = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5', '6.6.6.6', '7.7.7.7', '8.8.8.8', '9.9.9.9', '10.10.10.10']
hostnames = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10']

singleseg = [R5, R7, R8, R9, R10]
singlesegoct = ['5.5', '7.7', '8.8', '9.9', '10.10']
singleseglastoct = ['5', '7', '8', '9', '10']

seg146 = [R1, R4, R6]
octet146 =['1', '4', '6']

seg79 = [R7, R9]
octet79 =['7', '9']

seg67 = [R6, R7]
octet67 =['6', '7']

seg37 = [R3, R7]
octet37 =['3', '7']

seg13 = [R1, R3]
octet13 =['1', '3']

seg23 = [R2, R3]
octet23 =['2', '3']

seg45 = [R4, R5]
octet45 =['4', '5']
   
seg58 = [R5, R8]
octet58 =['5', '8']

seg108 = [R8, R10]
octet108 =['8', '10']
