# Raspberry Variable Fan Speed Install Procedure
The fanGo.py file is the program written in python for fan management. To be able to use it, make sure you have a python interpreter installed on your system.

If necessary, you can install the python interpreter using:   

    # apt-get install build-essential

## Using install file

To install automatically all required files and services run inside **fan folder** (as root):

    # bash fanInstall.sh

> a restart is required

## Manually

To start fanSystem.py automatically when the raspberry start, you need to use a linux service using **fanSystem.sh**.
The only thing to do, you have to edit the fanSystem.sh at line 15 before using it. In the line 15 you must specify in which folder the fanSystem.py and gpoClean.py files are located. 
So in line 15 you must insert your folder as:

    DIR=YOUR FOLDER HERE

After editing the file you must put the **fanSystem.sh** in the folder: 

    /etc/init.d

After change permission in the file with:

    # chmod u+x /etc/init.d/fanSystem.sh

Go to the folder:

    # cd /etc/init.d 

After you must enable the service with:
          
    # systemctl enable fanSystem.sh

and

    # update-rc.d fanSystem.sh defaults
    
Now you must change the permissions in **fanSystem.py** and **gpoClean.py** file using

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
