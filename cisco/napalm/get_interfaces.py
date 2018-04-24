"""
Correct Me If I am Wrong

MUHAMMAD HANIF
Website  : http://hanifmu.com
Email    : moehammadhanif@gmail.com
Telegram : https://t.me/muhammad_hanif
"""

from napalm import get_network_driver
from tabulate import tabulate
import argparse

def run(host, username, password, enable):
    driver = get_network_driver('ios')
    device = driver(hostname = host,
                    username = username,
                    password = password,
                    optional_args={'secret': enable})

    try:
        device.open()

        interfaces = device.get_interfaces()
        header = ['interface', 'is_enabled', 'is_up',
                  'speed', 'last_flapped', 'mac_address', 'description']
        table = [];

        for interface, interface_info in interfaces.items():
            is_enabled = 'True' if interface_info['is_enabled'] == 1 else 'False'
            is_up= 'True' if interface_info['is_up'] == 1 else 'False'

            table.append([interface, is_enabled,
                          is_up,
                          interface_info['speed'],
                          interface_info['last_flapped'],
                          interface_info['mac_address'],
                          interface_info['description']])

        print(tabulate(table, headers = header, tablefmt='grid'))

        device.close()
    except:
        print("We can't access {}. Check your credentials.".format(host))

if __name__ == '__main__':
    description = "This script will give you interface information: \n \
                   is_up  (True/False), is_enabled  (True/False),\
                   speed (in Mbit), last_flapped (in seconds), \
                   mac_address, and description."

    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("-ip", "--ip", required=True,
                        help="ip address of cisco device")
    parser.add_argument("-u", "--username", required=True,
                        help="username for accessing cisco device")
    parser.add_argument("-p", "--password", required=True,
                        help="password for accessing cisco device")
    parser.add_argument("-e", "--enable", required=True,
                        help="enable password for accessing cisco device")

    args = vars(parser.parse_args())

    run(args['ip'], args['username'], args['password'], args['enable'])
