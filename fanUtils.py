#!/usr/bin/env python

# fanUtils
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Most common functions to manage GPIO's pins

import os
import RPi.GPIO as GPIO
import fanConfig

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def gpio_clean():
    for gpio_fan_setting in fanConfig.GPIO_FAN_SETTINGS:
        GPIO.setup(gpio_fan_setting['gpio_name'], GPIO.OUT)
        GPIO.cleanup(gpio_fan_setting['gpio_name'])
        
def gpio_reset():
    gpio_setup()
    gpio_clean()

def gpio_on(gpio_number):
	GPIO.setup(gpio_number, GPIO.OUT)
	GPIO.output(gpio_number, 1)

def gpio_off(gpio_number):
	GPIO.cleanup(gpio_number)
        
def get_cpu_temperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return float(res.replace("temp=","").replace("'C\n",""))