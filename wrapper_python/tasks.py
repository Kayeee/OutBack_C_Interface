
from celery import Celery
from kombu import Queue

import subprocess
import random
import os
import socket
import fcntl
import struct
import json
import requests
import time

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HEMS.scripts.settings')

with open('/home/pi/HEMS/project/wrapper_python/system.json', 'r') as json_data:
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

results = {}

r = requests.get('http://192.168.0.102:8000/hems/wakeup', params=parameters)
results = r.json()
print(results)
rank = results["rank"]
if rank == "slave":
    master_isOn = results["master_isOn"]
    while not master_isOn:
        time.sleep(2)
        results = requests.get('http://192.168.0.102:8000/hems/wakeup', params=parameters)
        master_isOn = results.json()["master_isOn"]
        print("waiting for master")

    master_ip = results["master_local_ip"]
    app = Celery('interface_worker', backend='amqp', broker='amqp://Kevin:ASUi3dea@{0}/pi_env'.format(master_ip))
 #   CELERY_DEFAULT_QUEUE =str(parameters['box_id'])
#    CELERY_QUEUES = (Queue(str(parameters['box_id']), routing_key=str(parameters['box_id'])))
 
if rank == "master":
    slaves = []
    for slave_id in results["slaves"]:
        slaves.append(Queue(str(slave_id), routing_key=str(slave_id)))
    app = Celery('interface_worker', backend='amqp', broker='amqp://Kevin:ASUi3dea@192.168.0.102/pi_env')
#    CELERY_QUEUES = tuple(slaves)

#CELERY_DEFAULT_QUEUE = 'interface'
#CELERY_QUEUES = (Queue('interface', routing_key='interface'),
#    Queue('updater', routing_key='updater'),
#    Queue('outback', routing_key='outback'),)

@app.task(name='add')
def add(x, y):
    return x + y

def create_celery_queue(queue_name):
    CELERY_QUEUES.append(Queue(queue_name, routing_key=queue_name))
    # TODO: WRITE TO A FILE OR CREATE ALL QUEUES ON START UP FROM DATABASE

def create_celery_queue_temp(queue_name):
    CELERY_QUEUES.append(Queue(queue_name, routing_key=queue_name))
    return len(CELERY_QUEUES) - 1

def remove_celery_queue(index):
    pass

@app.task(name='check_device_status')
def check_device_status(hemsID):
    #TODO: write code that determines if pi is active
    return True

def initial_handshake(hemsID):
    # step 1 create queue
    queue = create_celery_queue(hemsID)
    # step 2 add task to queue
    status = check_device_status.apply_async(args=[hemsID], queue=queue, routing_key=queue)
    # step 3 look at result / register a timeout
    tries = 0
    while status.state != 'SUCCESS':
        print status.state
        tries += 1
        time.sleep(1)
        if tries > 4:
            return False

    return True

@app.task(name='getAlle')
def getAll(inverter_id):
    # inverter = Inverter()
    # result = inverter.getAlle("0")

    print("inverter id: {0}").format(inverter_id)
    return {"inverter_id": inverter_id}
