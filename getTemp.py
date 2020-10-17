#!/usr/bin/env python

import os
from time import sleep

def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        temp =(res.replace("temp=","").replace("'C\n",""))
        return temp

try:
	while True:
        	print(getCPUtemperature())
		sleep(1)
except:
	GPIO.cleanup()
