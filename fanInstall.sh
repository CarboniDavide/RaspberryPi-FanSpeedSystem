#!/bin/sh

# fanInstall v.1
# Carboni Corporation 2020- All right reserved https://www.carboni.ch
# Author: Carboni Davide
# @copyright Copyright (c) 2020, Carboni Software, Inc.
# @license AGPL-3.0
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License, version 3,
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Install fan system controll for Raspberry Pi


# set current directory in fanSystem and copy file in /etc/init.
sed "s|DIR=|DIR=$PWD|" fanSystem.sh > /etc/init.d/fanSystem.sh

# change folder's rights
chmod u+x /etc/init.d/fanSystem.sh
chmod u+x fanSystem.py
chmod u+x gpoClean.py

# enable fanSystem service
cd /etc/init.d
systemctl enable fanSystem.sh
update-rc.d fanSystem.sh defaults
