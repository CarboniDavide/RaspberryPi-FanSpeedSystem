# fanConfig v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
#
# Main project configuration file
#
# Use this file to config all GPIO's IN/OUT state
# Add new dictionary if you want to use more gpio's pin:
# for example add this at the end of array to have a new gpio pin: 
#  {
#       'gpio_name' : 8,
#       'temp_level' : 58
#  },
#
# In this base configuration four gpio's pin are useds 

GPIO_FAN_SETTINGS = [
    {
        'gpio_name' : 5,
        'temp_level' : 68
    },
    {
        'gpio_name' : 6,
        'temp_level' : 70
    },
    {
        'gpio_name' : 13,
        'temp_level' : 72
    },
    {
        'gpio_name' : 19,
        'temp_level' : 75
    }
]