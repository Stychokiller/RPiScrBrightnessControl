#!/bin/bash
#
# In order to use 'dialog', you must install it:
# sudo apt-get install dialog
# 'dialog' will display a small dialog box in a terminal window.
#
onOrOff=$1

if [ -z $DISPLAY ]; then
   # needed by xset functions...
   export DISPLAY=":0"
   #echo "Created the DISPLAY env variable"
fi

if [ $onOrOff == 0 ]; then
   xset c b s off
   xset -dpms
   xset s noblank
   echo "touchscreen blanking turned OFF."
   #dialog --title 'Raspberry Pi:' --begin 1 1 --msgbox 'screen blanking turned OFF!' 5 40
else
   xset c b s on
   xset dpms 3600 3600 3600
   xset s blank
   echo "touchscreen blanking turned ON."
   #dialog --title 'Raspberry Pi:' --begin 1 1 --msgbox 'screen blanking turned ON!' 5 40
fi
