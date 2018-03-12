# RPiScrBrightnessControl
Control Raspberry Pi touchscreen brightness from the desktop!
RPi Brightness program README:

In order to use this program you must have several wx-python packages
already installed:  libwxbase2.8-0:armhf, libwxgtk2.8-0:armhf, python-wxgtk3.0
& python-wxversion.

Be sure to edit the *.desktop file, especially the Icon, Exec & TryExec
entries to reflect WHERE you actually placed the files that you requested.
The *.desktop file goes in the pi/Desktop directory.

I would recommend placing all of the other script files (brightness.py,
brightnessFrame.py, setBrightness.sh, & stopBlanking.sh) in the /usr/local/sbin
directory. (works for me!)

stopBlanking.sh  is an extra script for killing touchscreen blanking (or
turning it on!)
