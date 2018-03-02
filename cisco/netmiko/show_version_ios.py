"""
Correct Me If I am Wrong

MUHAMMAD HANIF
Website  : http://hanifmu.com
Email    : moehammadhanif[@]gmail.com
Telegram : https://t.me/muhammad_hanif
"""

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '10.10.1.1',
    'username': 'hanif',
    'password': 'hanif',
    'secret':'hanif'
}

net_connect = ConnectHandler(**device)
show_version = net_connect.send_command('show version').splitlines()
show_version_ios = show_version[0].split(',')

print(show_version_ios[0])
print("-" *60)
print("IOS\t:", show_version_ios[1].strip())
print("Version\t:", show_version_ios[2].strip().split()[1])
