# confLoader
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
#
#  Project configuration loader
import json
import os
import sys

CONF_FILE_NAME = 'config.json'

GPIO_FAN_SETTINGS = []
FAN_REFRESH_TIME = None
TEST_SLEEP_TIME = None

def get_conf():
    global GPIO_FAN_SETTINGS 
    global FAN_REFRESH_TIME
    global TEST_SLEEP_TIME
    
    path = os.path.dirname(os.path.abspath(__file__))
    
    try:
        file = open(path + '/' + CONF_FILE_NAME, 'r')
    except:
        print("No JSON configuration file in : %s" % path)
      
    try:  
        data = json.load(file)
    except json.decoder.JSONDecodeError:
        print("String could not be converted to JSON")
    
    for c in data["GPIO_FAN_CONFIG"]:
        GPIO_FAN_SETTINGS.append({ str(key) : c[key] for key in c.keys() })
        
    FAN_REFRESH_TIME = float(data['FAN_REFRESH_TIME'])
    TEST_SLEEP_TIME = float(data['TEST_SLEEP_TIME'])
    
try:
    get_conf()
except:
    print("Error: Configuration not loaded")