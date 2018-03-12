#!/usr/bin/env python

#Boa:App:BoaApp

# WARNING:  you must already have libwxbase2.8-0:armhf,
# libwxgtk2.8-0:armhf  python-wxgtk3.0 & python-wxversion installed,
# otherwise, 'import wx' WILL NOT WORK!
#
import wx

import brightnessFrame

modules ={u'brightnessFrame': [1, 'Main frame of Application', u'brightnessFrame.py']}

class BoaApp(wx.App):
   def OnInit(self):
      self.main = brightnessFrame.create(None)
      self.main.Show()
      self.SetTopWindow(self.main)
      return True

def main():
   application = BoaApp(0)
   application.MainLoop()

if __name__ == '__main__':
   main()
