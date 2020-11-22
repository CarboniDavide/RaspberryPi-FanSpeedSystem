#!/usr/bin/env python

from time import sleep
import fanUtils

while True:
	print(fanUtils.get_cpu_temperature())
	sleep(1)

