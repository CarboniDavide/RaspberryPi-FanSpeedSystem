#!/bin/sh

# set current directory in fanSystem and copy file in /etc/init.
sed "s|DIR=|$PWD|" fanSystem.sh > /etc/init.d/fanSystem.sh

# change folder's rights
chmod u+x /etc/init.d/fanSystem.sh
chmod u+x fanSystem.py
chmod u+x gpoClean.py

# enable fanSystem service
systemctl enable fan-control.sh
update-rc.d fan-control.sh defaults
