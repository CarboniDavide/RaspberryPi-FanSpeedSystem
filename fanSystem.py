#!/usr/bin/env python

# fanSystem v.1
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Fan speed software control for Raspberry Pi

import time
import fanUtils, fanConfig

LOOP_SLEEP_TIME = 1
gpio_fan_states = [ { 'gpio_name': x['gpio_name'], 'temp_level': x['temp_level'], 'state' : 0 } for x in fanConfig.GPIO_FAN_SETTINGS ]
 
# prevent decorator: change gpio state when state change, do nothing elsewhere
def prevent(func):
    def function_wrapper(*args, **kwargs):
        current_fan_config = next(gpio_fan_state for gpio_fan_state in gpio_fan_states if gpio_fan_state["gpio_name"] == args[0])
        nex_state = args[1]
        
        if nex_state != current_fan_config['state']:
            current_fan_config['state'] = nex_state
            func(*args, **kwargs)
            
    return function_wrapper

# remove decorator if you don't want to have prevent configuration
@prevent
def gpio_set_state(gpio_number, state):
    fanUtils.gpio_on(gpio_number) if state == 1 else fanUtils.gpio_off(gpio_number)

def main():
    try:
        while True:
            cpu_temp = fanUtils.get_cpu_temperature()
            for gpio_fan_state in gpio_fan_states:
                gpio_set_state(gpio_fan_state['gpio_name'], 1 if cpu_temp > gpio_fan_state['temp_level'] else 0)
            
            time.sleep(LOOP_SLEEP_TIME) 
    except:
        fanUtils.gpio_clean()
    

# Entry Point -------
fanUtils.gpio_setup()
fanUtils.gpio_clean()
main()

