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
show_version = net_connect.send_command('show version')

print(show_version)

net_connect.disconnect()
