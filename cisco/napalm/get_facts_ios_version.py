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

facts = device.get_facts();
ios_version = facts['os_version'].split(',');

print("IOS\t:", ios_version[0].strip())
print("Version\t:", ios_version[1].strip().split()[1])

device.close()
