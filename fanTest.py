#!/usr/bin/env python

# fanTest v.1
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed test software for Raspberry Pi

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
from fanConfig import *

def gpio_setup():
        GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def gpio_clean():
    for fan_gpio_pin in FAN_GPIO_PINS:
        GPIO.setup(fan_gpio_pin, GPIO.OUT)
        GPIO.cleanup(fan_gpio_pin)
    return()

def increase():
        print("----------------------")
        print("STEP 1: FAN INCREASING")
        print("----------------------")

        for fan_level, gpio_pin in enumerate(FAN_GPIO_PINS, start= 1):
                print("Level %s is ON" % fan_level)
                GPIO.setup(gpio_pin, GPIO.OUT)
	        GPIO.output(gpio_pin, 1)
                sleep(3)

	return()

def decrease():
        print("----------------------")
        print("STEP 2: FAN DECREASING")
        print("----------------------")
        for fan_level, gpio_pin in enumerate(FAN_GPIO_PINS, start= 1):
                print("Level %s is OFF" % fan_level)
                GPIO.cleanup(gpio_pin)
                sleep(3)

	return()

gpio_setup()
gpio_clean()

try:
        increase()
        decrease()
except:
	gpio_clean()
