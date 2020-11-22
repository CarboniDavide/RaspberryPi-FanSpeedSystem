#!/usr/bin/env python

# gpoClean v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Clean all used gpio pins in fanSystem control software

import fanUtils

fanUtils.gpio_setup()
fanUtils.gpio_clean()