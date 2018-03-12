#!/bin/bash
#
# This script will work all by itself, but there is a wx-python program
# that I wrote that will display a GUI for this script!
#
level=$1
#echo "level given is $level"

if [ $# != 1 ]; then
   echo "USAGE: $0 brightness_level (0 to 255)"
   exit 1
fi

if [[ $level -ge 0 && $level -le 255 ]]; then
   #echo "level given is $level"
   #Make sure that the pi user has permissions for this...
   echo $level > /sys/class/backlight/rpi_backlight/brightness
   echo "Screen brightness set to $level."
   exit 0
else
   echo "Brightness level $level is out of range! (0 to 255 only)"
   exit 1
fi
