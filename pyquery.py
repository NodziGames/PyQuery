#Import Libraries
import wikipedia
import wolframalpha
import wx

#Configure APIs
wikipedia.set_lang("en")
app_id = "Insert Your API Key Here!"
client = wolframalpha.Client(app_id)

#GUI and functionality
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(420, 400),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
            wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyQuery"
            )
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="Query: ")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        self.answer = wx.TextCtrl(panel, size=(400,300), style=wx.TE_MULTILINE)
        self.answer.SetEditable(False)
        my_sizer.Add(self.answer, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    #Search
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            res = client.query(input)
            answertxt = "WOLFRAM SAYS: " + next(res.results).text
        except:
            answertxt = "WIKIPEDIA SAYS: " + wikipedia.summary(input)
        self.answer.SetValue(answertxt)
        del input

#Loop the app
if __name__== "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
