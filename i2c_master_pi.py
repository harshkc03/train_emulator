#!/usr/bin/python

import smbus
import time
bus = smbus.SMBus(1)
address = 0x2a

while True:
    data = ""
    start = time.time()
    for i in range(0, 15):
            data += chr(bus.read_byte(address))
    print(data)
    end = time.time()
    #print((end-start)*1000)
    time.sleep(1);