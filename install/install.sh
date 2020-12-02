#!/bin/sh

# install
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Install fanSystem controll for RaspberryPi as service

#get parent directory
APP_ROOT="$(dirname "$(dirname "$(readlink -fm "$0")")")"

# set current directory in fanSystem and copy file in /etc/init.
sed "s|DIR=|DIR=$APP_ROOT|" fanSystem > /etc/init.d/fanSystem

# change folder's rights
chmod u+x /etc/init.d/fanSystem
chmod u+x $APP_ROOT/fanSystem.py

# enable and register fanSystem service
cd /etc/init.d
systemctl enable fanSystem
update-rc.d fanSystem defaults

# start fanSystem service
systemctl start fanSystem