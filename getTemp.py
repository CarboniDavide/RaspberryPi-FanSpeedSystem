#!/usr/bin/env python

from time import sleep
import fanUtils

def main():
	while True:
		print("CPU temperature is: %s degrees celsius" % fanUtils.get_cpu_temperature())
		sleep(1)

if __name__ == "__main__":
    main()