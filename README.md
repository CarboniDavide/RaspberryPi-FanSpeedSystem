# Raspberry Pi Variable Fan Speed
The Raspberry Pi project allows you to manage the speed of the cooling fan, quickly and easily, without use additional electronic components

## Supported Devices
Actually this project has been tested and is available for: 

- Raspberry Pi 4
- Raspberry Pi 3
- Raspberry Pi 3 B+

## Required

- Python Interpreter

The fanSystem.py file is program written in python for fan management. To be able to use it, make sure you have a python interpreter installed on your system.

If necessary, you can install the python interpreter using:   

    # apt-get install build-essential

## How to Use
FanSystem application provide three basic functions:
- Run
- Clean
- Test

each of them can be called up in the command line as:

    # python fanSystem.py [-v, --verbose] -c <run | clean | test>

### Run
Basically function to start fan cooler engine:

    # python fanSystem.py -c run

### Test
Use this command to run a fast test for the current GPIO configuration:

    # python fanSystem.py -c test

### Clean
Use to clean and reset all used GPIO's pin:

    # python fanSystem.py -c clean


## How to install to run as service
To run fanSystem.py automatically when the RaspberryPi start, you need a linux service using **fanSystem** shell script file locate inside the **install folder**.
The **fanSystem** script file must be installed in your system before. Do it using **install file** or **manually**.

### Using install file
Go into **install** folder and run (as root) the follow command line:

    # bash install.sh

then verify service using:

    # service fanSystem status

### Manually

#### Step 1: Provide file informations and Copy
Go into **install** folder first and edit the **fanSystem** file at line 14 to specify in which folder fanSystem.py file is located. 
So in line 14 you must insert your project folder as:

    DIR=YOUR PROJECT FOLDER

After then, **copy fanSystem** shell script file into **/etc/init.d** folder.

#### Step 2: Permissions
Now in your project folder you must change permissions in **fanSystem.py** file using:
    
    # chmod u+x fanSystem.py

The same for **fanSystem** bash file into **init.d** folder:

    # chmod u+x /etc/init.d/fanSystem

#### Step 3: Enable and Link
Go into **init.d** folder:

    # cd /etc/init.d 

After then, you have to enable fanSystem service with:
          
    # systemctl enable fanSystem

and link it to load fanSystem service on system start:

    # update-rc.d fanSystem defaults
    
#### Step 4: Start and Check
Now start **fanSystem** service using:

    # service fanSystem start

and check using:

    # service fanSystem status.

> Try to restart system if service doesn't work after installation.

### How to Manage Service

To manage the service you can use: 

    service fanSystem start
    service fanSystem stop
    service fanSystem restart
    service fanSystem status
    service fanSystem reload
    service fanSystem force-reload