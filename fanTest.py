#!/usr/bin/env python

# fanTest v.1
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed test software for Raspberry Pi

import os
from time import sleep
import fanUtils, fanConfig

SLEEP_TIME = 1

def main():
        fanUtils.gpio_setup()
        fanUtils.gpio_clean()
        
        try:
                print("----------------------")
                print("STEP 1: FAN INCREASING")
                print("----------------------")
                for gpio_fan_setting in fanConfig.GPIO_FAN_SETTINGS:
                        print("GPIP %s is ON" % gpio_fan_setting['gpio_name'])
                        fanUtils.gpio_on(gpio_fan_setting['gpio_name'])
                        sleep(SLEEP_TIME)
                print("----------------------")
                print("STEP 2: FAN DECREASING")
                print("----------------------")
                for gpio_fan_setting in fanConfig.GPIO_FAN_SETTINGS:
                        print("GPIP %s is OFF" % gpio_fan_setting['gpio_name'])
                        fanUtils.gpio_off(gpio_fan_setting['gpio_name'])
                        sleep(SLEEP_TIME)
        except:
                fanUtils.gpio_clean()
        
if __name__ == "__main__":
    main()
