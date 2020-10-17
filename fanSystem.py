#!/usr/bin/env python

# fanSystem v.1
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed software control for Raspberry Pi

import os, time
import RPi.GPIO as GPIO
from fanConfig import *

LOOP_SLEEP_TIME = 5
fan_states= [0 ,0, 0, 0]

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def gpio_clean():
	for fan_gpio_pin in FAN_GPIO_PINS:
		GPIO.setup(fan_gpio_pin, GPIO.OUT)
		GPIO.cleanup(fan_gpio_pin)

def get_cpu_temperature():
	res = os.popen('vcgencmd measure_temp').readline()
	temp = (res.replace("temp=","").replace("'C\n",""))
	return float(temp)

def gpio_on(gpio_number):
	GPIO.setup(gpio_number, GPIO.OUT)
	GPIO.output(gpio_number, 1)

def gpio_off(gpio_number):
	GPIO.cleanup(gpio_number)

def fan_change_state(fan_level, fan_state):
	global fan_states

	if fan_states[fan_level] != fan_state:
		fan_states[fan_level] = fan_state
		gpio_on(FAN_GPIO_PINS[fan_level]) if fan_state == 1 else gpio_off(FAN_GPIO_PINS[fan_level])

def main():
	for fan_level, fan_temperature in enumerate(TEMPERATURE_LEVELS, start = 0):
		fan_change_state(fan_level, 1 if get_cpu_temperature() > fan_temperature else 0)

gpio_setup()
gpio_clean()

try:
	while True:
		main()
		time.sleep(LOOP_SLEEP_TIME)
except:
	gpio_clean()