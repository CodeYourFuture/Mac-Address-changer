#!/usr/bin/env python

import subprocess

interface = "wlan0"
mac_id = '40:49:0f:80:3c:7b'
new_mac = '40:49:0f:80:3c:5b'
current_id = "ifconfig wlan0 | grep ether"

print(f'[+] Changing MAC Address for {interface}  from {mac_id} to new mac')

subprocess.call(f'ifconfig {interface} down', shell=True)
subprocess.call(f'ifconfig wlan0 hw ether {new_mac}', shell=True)
subprocess.call('ifconfig wlan0 up', shell=True)
