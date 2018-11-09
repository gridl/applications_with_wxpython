# button_event.py

import wx


class MyPanel(wx.Panel):
    
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        
        button = wx.Button(self, label='Press Me')
        button.Bind(wx.EVT_BUTTON, self.on_button_press, button)
        
    def on_button_press(self, event):
        print('You pressed the button')

class MyFrame(wx.Frame):
    
    def __init__(self):
        super(MyFrame, self).__init__(None, title='Hello World')
        panel = MyPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()