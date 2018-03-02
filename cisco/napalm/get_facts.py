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

for key,value in facts.items():
    print("{0} : {1}".format(key,value))

device.close()
