#!/usr/bin/env python

# fanSystem
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed software control for Raspberry Pi

import time, sys, getopt, os
from fanUtils import *
from fanConfig import *

verbose_active = False
gpio_fan_states = { x['gpio_name'] : 0 for x in GPIO_FAN_SETTINGS }

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

# Core Functions -------------------------------------------------------

@prevent
def gpio_set_state(gpio_number, state):
    gpio_on(gpio_number) if state == 1 else gpio_off(gpio_number)
    gpio_fan_states[gpio_number] = state

@verbose("Starting cleanup process...", "Finished to cleanup! By")
def clean():
    gpio_reset()

@verbose("Start test process...", "Test completed succesfully! By")
@protect
def test():
    for gpio_fan_setting in GPIO_FAN_SETTINGS:
        gpio_on(gpio_fan_setting['gpio_name'])
        time.sleep(TEST_SLEEP_TIME)
    for gpio_fan_setting in GPIO_FAN_SETTINGS:
        gpio_off(gpio_fan_setting['gpio_name'])
        time.sleep(TEST_SLEEP_TIME)
    
@verbose("Start fan engine", "Fan engine terminated! By")
@protect
def run():
    while True:
        cpu_temp = get_cpu_temperature()
        for gpio_fan_state in GPIO_FAN_SETTINGS:
            gpio_set_state(gpio_fan_state['gpio_name'], 1 if cpu_temp > gpio_fan_state['temp_level'] else 0)
        time.sleep(FAN_REFRESH_TIME) 

# Main Functions --------------------------------------------------------   

def main(argv):
    
    global verbose_active
    
    try:
        opts, args = getopt.getopt(argv,"hvc:", ["help", "verbose", "command"])
    except getopt.GetoptError:
        print('fanSystem.py [-v, --verbose] -c <run | clean | test>')
        sys.exit(2)

    if not opts:
        run()
        sys.exit()

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('fanSystem.py [-v, --verbose] -c <run | clean | test>')
            sys.exit()
        if opt in ("-v", "--verbose"):
            verbose_active = True
        elif opt in ("-c", "--command"):
            if arg == "run":
                run()
            elif arg == "clean":
                clean()
            elif arg == "test":
                test()
            elif arg not in ["run", "clean", "test"]:
                 print('--> Use fanSystem.py [-v, --verbose] -c <run | clean | test>')
                
if __name__ == "__main__":
    main(sys.argv[1:])