#!/usr/bin/env python

import subprocess

subprocess.call('ifconfig wlan0 down', shell=True)
subprocess.call('ifconfig wlan0 hw ether 40:49:0f:80:3c:5b', shell=True)
subprocess.call('ifconfig wlan0 up', shell=True)
