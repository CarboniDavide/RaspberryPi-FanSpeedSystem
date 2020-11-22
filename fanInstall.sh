#!/bin/sh

# fanInstall v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Install fan system controll for Raspberry Pi

# set current directory in fanSystem and copy file in /etc/init.
sed "s|DIR=|DIR=$PWD|" fanSystem > /etc/init.d/fanSystem

# change folder's rights
chmod u+x /etc/init.d/fanSystem
chmod u+x fanSystem.py
chmod u+x gpoClean.py

# enable and register fanSystem service
cd /etc/init.d
systemctl enable fanSystem
update-rc.d fanSystem defaults

# start fanSystem service
systemctl start fanSystem