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

        facts = device.get_facts()
        table = [];

        for key,value in facts.items():
            table.append([key,value])

        print(tabulate(table, tablefmt='grid'))

        device.close()
    except:
        print("We can't access {}. Check your credentials.".format(host))

if __name__ == '__main__':
    description = 'To run this script, \
                  you must have credentials (username, password, and enable) \
                  for accessing your cisco device through SSH.'

    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("-ip", "--ip", required=True, help="ip address of cisco device")
    parser.add_argument("-u", "--username", required=True, help="username for accessing cisco device")
    parser.add_argument("-p", "--password", required=True, help="password for accessing cisco device")
    parser.add_argument("-e", "--enable", required=True, help="enable password for accessing cisco device")

    args = vars(parser.parse_args())

    run(args['ip'], args['username'], args['password'], args['enable'])
