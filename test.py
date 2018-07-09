 #!/usr/bin/env python3
import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

def setup():
        GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def Fan1ON():
	GPIO.setup(5, GPIO.OUT)
	GPIO.output(5, 1)
	print("Level One is ON")
	return()

def Fan2ON():
        GPIO.setup(6, GPIO.OUT)
        GPIO.output(6, 1)
	print("Level Two is ON")
        return()

def Fan3ON():
        GPIO.setup(13, GPIO.OUT)
        GPIO.output(13, 1)
	print("Level Three is ON")
        return()

def Fan4ON():
        GPIO.setup(19, GPIO.OUT)
        GPIO.output(19, 1)
	print("Level Four is ON")
        return()

def Fan1OFF():
        GPIO.output(5, 0)
        GPIO.cleanup(5)
	print("Level One is OFF")
        return()

def Fan2OFF():
        GPIO.output(6, 0)
        GPIO.cleanup(6)
	print("Level Two is OFF")
        return()

def Fan3OFF():
        GPIO.output(13, 0)
        GPIO.cleanup(13)
	print("Level Three is OFF")
        return()

def Fan4OFF():
        GPIO.output(19, 0)
        GPIO.cleanup(19)
	print("Level Four is OFF")	
        return()

setup()
GPIO.cleanup()
print("----------------------")
print("STEP 1: FAN INCREASING")
print("----------------------")
print("")
sleep(3)
Fan1ON()
sleep(5)
Fan2ON()
sleep(5)
Fan3ON()
sleep(5)
Fan4ON()
sleep(5)
print("")
print("----------------------")
print("STEP 2: FAN DECREASING")
print("----------------------")
print("")
sleep(3)
Fan1OFF()
sleep(5)
Fan2OFF()
sleep(5)
Fan3OFF()
sleep(5)
Fan4OFF()

GPIO.cleanup()
