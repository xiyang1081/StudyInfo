#!/usr/bin/env python
#coding=utf-8

import wx
class Frame(wx.Frame):
    pass

class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title='Bare')
        frame.Show()
        return True

app=App()
app.MainLoop()
