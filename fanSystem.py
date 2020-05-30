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

#temperatures levels

TEMP_LV_1 = 55
TEMP_LV_2 = 60
TEMP_LV_3 = 62
TEMP_LV_4 = 65

#Controls flags

Fan1ON = False
Fan2ON = False
Fan3ON = False
Fan4ON = False

#GPIO pins

Fan1 = 5
Fan2 = 6
Fan3 = 13
Fan4 = 19

#timer

TimeSleep = 3

def setup():
        GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def clean():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(5, GPIO.OUT)
	GPIO.setup(6, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(19, GPIO.OUT)
	GPIO.cleanup()
	return()

def init():
	clean()
	setup()
	return()

def getCPUtemperature():
        res = os.popen('vcgencmd measure_temp').readline()
        temp =(res.replace("temp=","").replace("'C\n",""))
        return temp

def Switch_ON(n_fun):
	GPIO.setup(n_fun, GPIO.OUT)
	GPIO.output(n_fun, 1)
	return True

def Switch_OFF(n_fun):
        GPIO.cleanup(n_fun)
        return False

def fanON(n_fun):

	global Fan1ON
	global Fan2ON
	global Fan3ON
	global Fan4ON

	if n_fun == 1 and Fan1ON == False:
		Fan1ON = Switch_ON(Fan1)

	if n_fun == 2 and Fan2ON == False:
                Fan2ON = Switch_ON(Fan2)

	if n_fun == 3 and Fan3ON == False:
                Fan3ON = Switch_ON(Fan3)

	if n_fun == 4 and Fan4ON == False:
                Fan4ON = Switch_ON(Fan4)

        return()

def fanOFF(n_fun):

	global Fan1ON
        global Fan2ON
        global Fan3ON
        global Fan4ON

	if n_fun == 4 and Fan4ON == True:
                Fan4ON = Switch_OFF(Fan4)

        if n_fun == 3 and Fan3ON == True:
                Fan3ON = Switch_OFF(Fan3)

        if n_fun == 2 and Fan2ON == True:
                Fan2ON = Switch_OFF(Fan2)

        if n_fun == 1 and Fan1ON == True:
                Fan1ON = Switch_OFF(Fan1)

        return()

def ControlFan():
        CPU_temp = float(getCPUtemperature())

	if CPU_temp > TEMP_LV_1:
		fanON(1)
        else:
		fanOFF(1)

	if CPU_temp > TEMP_LV_2:
                fanON(2)
        else:
                fanOFF(2)

	if CPU_temp > TEMP_LV_3:
                fanON(3)
        else:
                fanOFF(3)

	if CPU_temp > TEMP_LV_4:
                fanON(4)
        else:
                fanOFF(4)

        sleep(TimeSleep)
        return()

init()

try:
	while True:
        	ControlFan()
except:
	GPIO.cleanup()
