from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import time
import subprocess


# Global variable
register_list = ['OutBack_Minute']
write_values = ['3']
queue = '1'


def call_write_task():
    if len(register_list) != len(write_values):
        return False
    result = subprocess.Popen(['python', 'write_outback_registers.py']+register_list+write_values, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = result.communicate()
    if result.returncode != 0:
        print('stderr: [%s]' % err)
        print('stderr: [%s]' % out)
        return False
    return True


def call_read_task():
    result = subprocess.Popen(['python', 'read_outback_registers.py']+register_list, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    err, out = result.communicate()
    if result.returncode != 0:
        print('stderr: [%s]' % err)
        print('stderr: [%s]' % out)
        return False
    return True


def performScheduledTasks():
    scheduler = BlockingScheduler()
    scheduler.add_job(call_read_task, 'interval', minutes=5)
    scheduler.add_job(call_write_task, 'interval', minutes=15)
    scheduler.start()

if __name__=='__main__':
    performScheduledTasks()
