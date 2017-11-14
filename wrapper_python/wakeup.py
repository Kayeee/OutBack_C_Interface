#!/usr/bin/python

import requests
import time
import logging
import sys
import json

def setup_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('../logs/wakeup.log', mode='a')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

#time.sleep(30)
logger = setup_logger('wakeup')
logger.info('Here')

logging.basicConfig(filename='../logs/wakeup.log', level=logging.DEBUG)

with open('system.json', 'r') as json_data:
    d = json.load(json_data)
    print(d["system"]["box_id"])
    parameters = d["system"]
   
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print(get_ip_address('wlan0'))
parameters['local_ip'] = get_ip_address('wlan0')
r = requests.get('http://192.168.0.101:8000/wakeup', params=parameters)
print(r.json())

