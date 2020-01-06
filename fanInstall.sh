#!/bin/sh

# set current directory in fanSystem and copy file in /etc/init.
sed "s|DIR=|$PWD|" fanSystem.sh > /etc/init.d/fanSystem.sh

# change folder's rights
chmod u+x /etc/init.d/fanSystem.sh
chmod u+x fanSystem.py
chmod u+x gpoClean.py

# enable fanSystem service
cd /etc/init.d
systemctl enable fanSystem.sh
update-rc.d fanSystem.sh defaults
