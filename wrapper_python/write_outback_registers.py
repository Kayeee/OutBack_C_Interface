import sys
import InverterFactory
import logging
import csv
import json
import datetime
import re
import os.path
import requests
from read_outback_registers import *


def write_values(register_list, write_values):

    inv = InverterFactory.InverterFactory().factory()
    # Process each register by passing its values to local memory and database
    for index in range(len(register_list)):
        register = register_list[index]
        value = write_values[index]
        write_result = str(inv.write(register,value))
        print(write_result)


if __name__ == '__main__':
    # A register list assigned by task
    register_list = sys.argv[1]
    write_values = sys.argv[2]
    write_values(register_list, write_values)
    progress(register_list)