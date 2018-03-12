# Gasp, yes, I have been known to use Boa-Constructor!
#Boa:Frame:stbFrame

# WARNING:  you must already have libwxbase2.8-0:armhf,
# libwxgtk2.8-0:armhf  python-wxgtk3.0 & python-wxversion installed,
# otherwise, 'import wx' WILL NOT WORK!
#

import wx
import os

def create(parent):
   return stbFrame(parent)

[wxID_STBFRAME, wxID_STBFRAMEBRTLEVEL, wxID_STBFRAMEDONEBT,
 wxID_STBFRAMELEVELSTR, wxID_STBFRAMEMAXLEVELBT, wxID_STBFRAMEMINLEVELBT,
] = [wx.NewId() for _init_ctrls in range(6)]

class stbFrame(wx.Frame):
   brightLevel = 100 # default value.
   # Use my script file that sets the Brightness hardware variable:
   brtCmd      = '/usr/local/sbin/setBrightness.sh'

   def _init_ctrls(self, prnt):
      wx.Frame.__init__(self, id=wxID_STBFRAME, name=u'stbFrame', parent=prnt,
            pos=wx.Point(20, 25), size=wx.Size(600, 120),
            style=wx.DEFAULT_FRAME_STYLE, title=u'Set Touchscreen Brightness:')
      self.SetClientSize(wx.Size(600, 120))

      self.brtLevel = wx.Slider(id=wxID_STBFRAMEBRTLEVEL, maxValue=255,
            minValue=0, name=u'brtLevel', parent=self, pos=wx.Point(20, 20),
            size=wx.Size(500, 29), style=wx.SL_HORIZONTAL, value=20)
      self.brtLevel.SetLabel(u'Brightness')
      self.brtLevel.SetThumbLength( 90 )
      self.brtLevel.SetRange( 0, 255 )
      self.brtLevel.Bind(wx.EVT_LEFT_UP, self.OnBrtLevelLeftUp)
      self.brtLevel.Bind(wx.EVT_SCROLL, self.OnBrtLevelScroll)

      self.levelStr = wx.TextCtrl(id=wxID_STBFRAMELEVELSTR, name=u'levelStr',
            parent=self, pos=wx.Point(520, 20), size=wx.Size(60, 32), style=0,
            value=u'100')
      self.levelStr.SetEditable(False)
      self.levelStr.SetToolTipString(u'Brightness Level')
      self.levelStr.SetMaxLength(3)

      self.minLevelBt = wx.Button(id=wxID_STBFRAMEMINLEVELBT,
            label=u'&Minimize', name=u'minLevelBt', parent=self,
            pos=wx.Point(30, 60), size=wx.Size(110, 33), style=0)
      self.minLevelBt.SetToolTipString(u'Dim Screen')
      self.minLevelBt.Bind(wx.EVT_LEFT_UP, self.OnMinLevelBtLeftUp)

      self.maxLevelBt = wx.Button(id=wxID_STBFRAMEMAXLEVELBT,
            label=u'Ma&ximize', name=u'maxLevelBt', parent=self,
            pos=wx.Point(456, 60), size=wx.Size(110, 33), style=0)
      self.maxLevelBt.Bind(wx.EVT_LEFT_UP, self.OnMaxLevelBtLeftUp)

      self.doneBt = wx.Button(id=wxID_STBFRAMEDONEBT, label=u'D&ONE!',
            name=u'doneBt', parent=self, pos=wx.Point(250, 60), size=wx.Size(86,
            33), style=0)
      self.doneBt.Bind(wx.EVT_LEFT_UP, self.OnDoneBtLeftUp)

   def __init__(self, parent):
      self._init_ctrls(parent)

   def setBrightnessVariable( self, brtLevel ):
      #print 'Executing ', self.brtCmd + " " + str( brtLevel ), '...'
      result = os.system( self.brtCmd + " " + str( brtLevel ) )
      return result

   def OnBrtLevelScroll(self, event):
      currentLevel = self.brtLevel.GetValue()
      if currentLevel != self.brightLevel:
         self.brightLevel = currentLevel
         self.levelStr.SetValue( str( self.brightLevel ) )
      event.Skip()

   def OnBrtLevelLeftUp(self, event):
      currentLevel = self.brtLevel.GetValue()
      self.brightLevel = currentLevel
      self.levelStr.SetValue( str( self.brightLevel ) )
      event.Skip()

   def OnMinLevelBtLeftUp(self, event):
      self.brightLevel = 10
      self.brtLevel.SetValue( self.brightLevel )
      self.levelStr.SetValue( str( self.brightLevel ) )
      event.Skip()

   def OnMaxLevelBtLeftUp(self, event):
      self.brightLevel = 250
      self.brtLevel.SetValue( self.brightLevel )
      self.levelStr.SetValue( str( self.brightLevel ) )
      event.Skip()

   def OnDoneBtLeftUp(self, event):
      self.brtLevel.SetValue( self.brightLevel )
      #print 'brightness level is', self.brightLevel
      self.setBrightnessVariable( self.brightLevel )
      self.Destroy()
