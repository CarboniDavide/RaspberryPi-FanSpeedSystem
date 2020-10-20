# Raspberry Pi Variable Fan Speed
The Raspberry Pi project allows you to manage the speed of the cooling fan, quickly and easily, without use additional electronic components
> [See The Video Tutorial](https://www.youtube.com/watch?v=ZGZ9NysbaRc&t)

## Supported Devices
Actually this project has been tested and is available for: 

- Raspberry Pi 4
- Raspberry Pi 3

## Required

- Python Interpreter

The fanSystem.py file is program written in python for fan management. To be able to use it, make sure you have a python interpreter installed on your system.

If necessary, you can install the python interpreter using:   

    # apt-get install build-essential

## How to Install

### Using install file
To install automatically all required files and services run inside your project folder (as root):

    # bash fanInstall.sh

then verify service using:

    # systemctl status fanSystem

or 

    # service fanSystem status

### Manually

#### Step 1: Provide file informations and Copy
To start fanSystem.py automatically when the raspberry start, you need to use a linux service using **fanSystem** shell script file.
The only thing to do, you have to edit the **fanSystem** file at line 14 before using it. In the line 14 you must specify in which folder fanSystem.py and gpoClean.py files are located. 
So in line 14 you must insert your project folder as:

    DIR=YOUR FOLDER HERE

After then, **copy fanSystem** shell script file into **/etc/init.d** folder.

#### Step 2: Permissions
Now in your project folder you must change permissions in **fanSystem.py** and **gpoClean.py** file using:
    
    # chmod u+x fanSystem.py
    # chmod u+x gpoClean.py

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

> The gpoClean.py file is a small program used only to clear all GPIO pins when the service start or restart.

> Try to restart system if service doesn't work after installation.

## How to Manage Service

To manage the service you can use: 

    service fanSystem start
    service fanSystem stop
    service fanSystem restart
    service fanSystem status
    service fanSystem reload
    service fanSystem force-reload
