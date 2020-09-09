#!/usr/bin/env python
import RPi.GPIO as GPIO

FAN_GPIO_PINS= [5, 6, 13, 19]

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def gpio_clean():
    for fan_gpio_pin in FAN_GPIO_PINS:
        GPIO.setup(fan_gpio_pin, GPIO.OUT)
        GPIO.cleanup(fan_gpio_pin)
    return()

gpio_setup()
gpio_clean()