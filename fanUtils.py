#!/usr/bin/env python

# fanUtils
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Most common functions to manage GPIO's pins

import os
import RPi.GPIO as GPIO
from fanConfig import GPIO_FAN_SETTINGS

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
        
def gpio_set(gpio_number, state):
	GPIO.setup(gpio_number, GPIO.OUT)
	GPIO.output(gpio_number, 1) if state else GPIO.cleanup(gpio_number)
 
def gpio_reset():
    gpio_setup()
    [gpio_set(gpio['gpio_name'], 0) for gpio in GPIO_FAN_SETTINGS]
        
def get_cpu_temperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return float(res.replace("temp=","").replace("'C\n",""))