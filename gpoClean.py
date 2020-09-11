#!/usr/bin/env python

# gpoClean v.1
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Clean all used gpio pins in fanSystem control software

import RPi.GPIO as GPIO
from fanConfig import *

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def gpio_clean():
    for fan_gpio_pin in FAN_GPIO_PINS:
        GPIO.setup(fan_gpio_pin, GPIO.OUT)
        GPIO.cleanup(fan_gpio_pin)

gpio_setup()
gpio_clean()