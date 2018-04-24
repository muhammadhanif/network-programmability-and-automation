# NETWORK PROGRAMMABILITY AND AUTOMATION
To run the script, you must add arguments (IP address, username, password, and enable).

Example:
```
python script.py -ip 10.10.1.1 -u hanif -p hanif -e hanif
```

```
python script.py -ip 10.10.1.1 --username hanif --password hanif --enable hanif
```

### [get_facts.py](https://github.com/muhammadhanif/network-programmability-and-automation/blob/master/cisco/napalm/get_facts.py)

This script will give you the following information:
* uptime - Uptime of the device in seconds.
* vendor - Manufacturer of the device.
* model - Device model.
* hostname - Hostname of the device
* fqdn - Fqdn of the device
* os_version - String with the OS version running on the device.
* serial_number - Serial number of the device
* interface_list - List of the interfaces of the device

How to run:
```
python get_facts.py -h
```
