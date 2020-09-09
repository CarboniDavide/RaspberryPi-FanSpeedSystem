#!/usr/bin/env python

# fanSystem v.1
# Carboni Corporation 2017- All right reserved https://www.carboni.ch
# Author: Carboni Davide
# @copyright Copyright (c) 2017, Carboni Software, Inc.
# @license AGPL-3.0
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License, version 3,
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Fan speed software control for Raspberry Pi 3

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

TEMPERATURE_LEVELS= [67, 70, 72, 75]
FAN_GPIO_PINS= [5, 6, 13, 19]
LOOP_SLEEP_TIME = 3

fan_states= [0 ,0, 0, 0]

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def gpio_clean():
	global fan_states

	for fan_gpio_pin in FAN_GPIO_PINS:
		GPIO.setup(fan_gpio_pin, GPIO.OUT)
		GPIO.cleanup(fan_gpio_pin)

	fan_states= [0 ,0, 0, 0]
	return()

def get_cpu_temperature():
	res = os.popen('vcgencmd measure_temp').readline()
	temp =(res.replace("temp=","").replace("'C\n",""))
	return temp

def gpio_on(gpio_number):
	GPIO.setup(gpio_number, GPIO.OUT)
	GPIO.output(gpio_number, 1)
	return()

def gpio_off(gpio_number):
	GPIO.cleanup(gpio_number)
	return()

def fan_prevent_change(fan_level, fan_state):
	return True if fan_states[fan_level] == fan_state else False

def fan_change_state(fan_level, fan_state):
	global fan_states

	if fan_prevent_change(fan_level, fan_state):
		return()
	
	fan_states[fan_level]= fan_state
	gpio= FAN_GPIO_PINS[fan_level]
	gpio_on(gpio) if fan_state == 1 else gpio_off(gpio)
	return()

def main():
	cpu_temp = float(get_cpu_temperature())
	
	for fan_level, fan_temperature in enumerate(TEMPERATURE_LEVELS, start=0):
		fan_change_state(fan_level, 1 if cpu_temp > fan_temperature else 0)

	sleep(LOOP_SLEEP_TIME)
	return()

gpio_setup()
gpio_clean()

try:
	while True:
        	main()
except:
	gpio_clean()