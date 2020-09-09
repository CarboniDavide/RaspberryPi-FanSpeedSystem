#!/usr/bin/env python3
import os
import time
import sys

TEMPERATURE_LEVELS= [67 , 70, 72, 75]

fan1On = False
fan2On = False
fan3On = False
fan4On = False

LVL_1 = TEMPERATURE_LEVELS[0]
LVL_2 = TEMPERATURE_LEVELS[1]
LVL_3 = TEMPERATURE_LEVELS[2]
LVL_4 = TEMPERATURE_LEVELS[3]

TimeRefr = 0.5

def VideoPrint(temp):
	global fan1On
        global fan2On
        global fan3On
        global fan4On

	os.system('clear')
	print("***********************************")
	print("* temp: {0}                      *".format(temp))
	print("*                                 *")
	print("* Refresh Time: 0.3s              *")
	print("*                                 *")
	print("* FAN LEVELS STATUS               *")
	print("*                                 *")
	if fan1On == True:
		print '\033[1;33m* ['+str(LVL_1)+' C] Level One          -> ON *\033[1;m'
	else:
		print("* ["+str(LVL_1)+" C] Level One         -> OFF *")
	if fan2On == True:
                print'\033[1;33m* ['+str(LVL_2)+' C] Level Two          -> ON *\033[1;m'
        else:
                print("* ["+str(LVL_2)+" C] Level Two         -> OFF *")
	if fan3On == True:
                print'\033[1;33m* ['+str(LVL_3)+' C] Level Three        -> ON *\033[1;m'
        else:
                print("* ["+str(LVL_3)+" C] Level Three       -> OFF *")
	if fan4On == True:
                print'\033[1;33m* ['+str(LVL_4)+' C] Level Four         -> ON *\033[1;m'
        else:
                print("* ["+str(LVL_4)+" C] Level Four        -> OFF *")
	print("*                                 *")
	print("***********************************")


def tempMonitor(temp):
	global fan1On
        global fan2On
        global fan3On
        global fan4On

	if temp >= LVL_1 and fan1On == False:
                fan1On = True
        if temp >= LVL_2 and fan2On == False:
                fan2On = True
        if temp >= LVL_3 and fan3On == False:
                fan3On = True
        if temp >= LVL_4 and fan4On == False:
                fan4On = True

        if temp < LVL_1 and fan1On == True:
                fan1On = False
        if temp < LVL_2 and fan2On == True:
                fan2On = False
        if temp < LVL_3 and fan3On == True:
                fan3On = False
        if temp < LVL_4 and fan4On == True:
                fan4On = False

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	_temp =(res.replace("temp=","").replace("'C\n",""))
	return float(_temp)
try:
    	while True:
        	CPUtemp = getCPUtemperature()
		tempMonitor(CPUtemp)
		VideoPrint(CPUtemp)
		time.sleep(TimeRefr)

except KeyboardInterrupt:
	print("Carboni Solutions Software")
