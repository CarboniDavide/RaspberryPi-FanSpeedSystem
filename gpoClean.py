#!/usr/bin/env python

# gpoClean v.2
# Carboni Corporation 2020 - All right reserved https://www.carboni.ch
# Clean all used gpio pins in fanSystem control software

import fanUtils

def main():
    fanUtils.gpio_setup()
    fanUtils.gpio_clean()

if __name__ == "__main__":
    main()