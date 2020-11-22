#!/usr/bin/env python

# gpoClean v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Get CPU temperature

from time import sleep
import fanUtils

def main():
	while True:
		print("CPU temperature is: %s degrees celsius" % fanUtils.get_cpu_temperature())
		sleep(1)

if __name__ == "__main__":
    main()