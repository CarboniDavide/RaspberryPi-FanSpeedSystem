#!/usr/bin/env python

# getTemp v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Get cpu temperature

from time import sleep
import fanUtils

while True:
	print(fanUtils.get_cpu_temperature())
	sleep(1)

