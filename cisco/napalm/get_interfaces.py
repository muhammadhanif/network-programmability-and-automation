"""
Correct Me If I am Wrong

MUHAMMAD HANIF
Website  : http://hanifmu.com
Email    : moehammadhanif@gmail.com
Telegram : https://t.me/muhammad_hanif
"""

from napalm import get_network_driver

driver = get_network_driver('ios')
device = driver(hostname='10.10.1.1',
                username='hanif',
                password='hanif',
                optional_args={'secret': 'hanif'})
device.open()

interfaces = device.get_interfaces()

#print(interfaces)

print("\n")
print("-" * 150)
print("{:^30}{}{:^15}{}{:^10}{}{:^10}{}{:^15}{}{:^25}{}{:^20}".format('interface', '|' ,'is_enabled', '|', 'is_up', '|', 'speed', '|', 'last_flapped', '|', 'mac_address', '|', 'description'))
print("-" * 150)

for interface, interface_info in interfaces.items():
    is_enabled = 'True' if interface_info['is_enabled'] == 1 else 'False'
    is_up= 'True' if interface_info['is_up'] == 1 else 'False'

    print("{:^30}{}{:^15}{}{:^10}{}{:^10}{}{:^15}{}{:^25}{}{:^20}".format(interface, '|', is_enabled, '|',  is_up, '|', interface_info['speed'], '|', interface_info['last_flapped'], '|', interface_info['mac_address'], '|', interface_info['description']))

print("-" * 150)

print('\n')

device.close()
