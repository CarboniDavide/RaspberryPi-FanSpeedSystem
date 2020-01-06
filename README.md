# Raspberry Variable Fan Speed Install Procedure

## Using install file

To install automatically all required files and services run inside **fan folder** (as root):

    # bash fanInstall.sh

> a restart is required

## Manually

The fanGo.py file is the program written in python for fan management. To be able to use it, make sure you have a python interpreter installed on your system.

For example, you can install the python interpreter using:   

    # apt-get install build-essential

After to verify if it work run the fanGo.py program, type the command: 

    # python fanGo.py 

To start fanGo.py automatically when the raspberry start, you need to use a linux service using fan-control.sh.
The only thing to do, you have to edit the fan-control.sh at line 15 before using it. In the line 15 you must specify in which folder the fanGo.py and init.py files are located. 
In line 15 you will find this:

    DIR= ---> YOUR FOLDER HERE <---

After editing the file you must put the fan-control.sh in the folder: 

    /etc/init.d

After change permission in the file with:

    # chmod u+x /etc/init.d/fanSystem.sh

Go to the folder:

    # cd /etc/init.d 

After you must enable the service with:
          
    # systemctl enable fanSystem.sh

and

    # update-rc.d fanSystem.sh defaults
    
Now you must change the permissions in "fanGo.py" and "init.py" file using

    # chmod u+x fanSystem.py
    
and

    # chmod u+x gpoClean.py

After restart your system and verify if the fan-control service is running correctly using the command: 

    # service fanSystem status.

To manage the service you can use: 

    service fanSystem start
    service fanSystem stop
    service fanSystem restart
    service fanSystem status
    service fanSystem reload
    service fanSystem force-reload

The gpoClean.py file is a small program that is used only to clear all GPIO pins when the service start or is reloaded.
