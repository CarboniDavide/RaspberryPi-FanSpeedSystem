#!/usr/bin/env python

# fanSystem
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed software control for Raspberry Pi

import time
import sys
import getopt
import os
import RPi.GPIO as GPIO
from config import *

verbose_active = False
gpio_fan_states = {x['gpio_name']: 0 for x in GPIO_FAN_SETTINGS}


# Utils ----------------------------------------------------------------


def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


def gpio_set(gpio_number, state):
    GPIO.setup(gpio_number, GPIO.OUT)
    GPIO.output(gpio_number, 1) if state else GPIO.cleanup(gpio_number)


def gpio_reset():
    gpio_setup()
    [gpio_set(gpio['gpio_name'], 0) for gpio in GPIO_FAN_SETTINGS]


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))


# Decorators -------------------------------------------------------------


def verbose(before="Process started...", after="Process terminated. Bye!"):
    def f_verbose(func):
        def w_verbose(*args, **kwargs):
            if verbose_active:
                print(before)

            func(*args, **kwargs)

            if verbose_active:
                print(after)

        return w_verbose
    return f_verbose


def prevent(func):
    def w_prevent(*args, **kwargs):
        current_state = gpio_fan_states[args[0]]
        nex_state = args[1]

        if nex_state != current_state:
            func(*args, **kwargs)

    return w_prevent


def protect(func):
    def w_prevent(*args, **kwargs):
        gpio_reset()
        try:
            func(*args, **kwargs)
        except:
            gpio_reset()
    return w_prevent


# Core -----------------------------------------------------------------


@prevent
def gpio_set_state(gpio_number, state):
    gpio_set(gpio_number, state)
    gpio_fan_states[gpio_number] = state


@verbose("Starting cleanup process...", "Finished to cleanup! By")
def clean():
    gpio_reset()


@verbose("Start test process...", "Test completed succesfully! By")
@protect
def test():
    for state in [1, 0]:
        for gpio in GPIO_FAN_SETTINGS:
            gpio_set(gpio['gpio_name'], state)
            time.sleep(TEST_SLEEP_TIME)


@verbose("Start fan engine", "Fan engine terminated! By")
@protect
def run():
    while True:
        cpu_temp = get_cpu_temperature()
        for gpio in GPIO_FAN_SETTINGS:
            gpio_set_state(gpio['gpio_name'], 1 if cpu_temp > gpio['temp_level'] else 0)
        time.sleep(FAN_REFRESH_TIME)


# Main -------------------------------------------------------------------


def main(argv):

    def usage():
        print('--> Use fanSystem.py [-v, --verbose] -c <run | clean | test>')
        sys.exit(2)

    global verbose_active

    try:
        opts, args = getopt.getopt(argv, "hvc:", ["help", "verbose", "command"])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-v", "--verbose"):
            verbose_active = True
        elif opt in ("-c", "--command"):
            eval(arg + "()") if arg in ["run", "clean", "test"] else usage()
            sys.exit()

    usage()


if __name__ == "__main__":
    main(sys.argv[1:])
