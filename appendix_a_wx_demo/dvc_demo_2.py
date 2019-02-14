# dvc_demo_2.py

import wx
import wx.dataview as dv

musicdata = {
1 : ("Bad English", "The Price Of Love", "Rock"),
2 : ("DNA featuring Suzanne Vega", "Tom's Diner", "Rock"),
3 : ("George Michael", "Praying For Time", "Rock"),
4 : ("Gloria Estefan", "Here We Are", "Rock"),
5 : ("Linda Ronstadt", "Don't Know Much", "Rock"),
6 : ("Michael Bolton", "How Am I Supposed To Live Without You", "Blues"),
7 : ("Paul Young", "Oh Girl", "Rock"),
8 : ("Paula Abdul", "Opposites Attract", "Rock"),
9 : ("Richard Marx", "Should've Known Better", "Rock"),
10: ("Rod Stewart", "Forever Young", "Rock"),
11: ("Roxette", "Dangerous", "Rock"),
12: ("Sheena Easton", "The Lover In Me", "Rock"),
13: ("Sinead O'Connor", "Nothing Compares 2 U", "Rock"),
14: ("Stevie B.", "Because I Love You", "Rock"),
15: ("Taylor Dayne", "Love Will Lead You Back", "Rock"),
16: ("The Bangles", "Eternal Flame", "Rock"),
17: ("Wilson Phillips", "Release Me", "Rock"),
18: ("Billy Joel", "Blonde Over Blue", "Rock"),
19: ("Billy Joel", "Famous Last Words", "Rock"),
20: ("Janet Jackson", "State Of The World", "Rock"),
21: ("Janet Jackson", "The Knowledge", "Rock"),
22: ("Spyro Gyra", "End of Romanticism", "Jazz"),
23: ("Spyro Gyra", "Heliopolis", "Jazz"),
24: ("Spyro Gyra", "Jubilee", "Jazz"),
25: ("Spyro Gyra", "Little Linda", "Jazz"),
26: ("Spyro Gyra", "Morning Dance", "Jazz"),
27: ("Spyro Gyra", "Song for Lorraine", "Jazz"),
28: ("Yes", "Owner Of A Lonely Heart", "Rock"),
29: ("Yes", "Rhythm Of Love", "Rock"),
30: ("Billy Joel", "Lullabye (Goodnight, My Angel)", "Rock"),
31: ("Billy Joel", "The River Of Dreams", "Rock"),
32: ("Billy Joel", "Two Thousand Years", "Rock"),
33: ("Janet Jackson", "Alright", "Rock"),
34: ("Janet Jackson", "Black Cat", "Rock"),
35: ("Janet Jackson", "Come Back To Me", "Rock"),
36: ("Janet Jackson", "Escapade", "Rock"),
37: ("Janet Jackson", "Love Will Never Do (Without You)", "Rock"),
38: ("Janet Jackson", "Miss You Much", "Rock"),
39: ("Janet Jackson", "Rhythm Nation", "Rock"),
40: ("Cusco", "Dream Catcher", "New Age"),
41: ("Cusco", "Geronimos Laughter", "New Age"),
42: ("Cusco", "Ghost Dance", "New Age"),
43: ("Blue Man Group", "Drumbone", "New Age"),
44: ("Blue Man Group", "Endless Column", "New Age"),
45: ("Blue Man Group", "Klein Mandelbrot", "New Age"),
46: ("Kenny G", "Silhouette", "Jazz"),
47: ("Sade", "Smooth Operator", "Jazz"),
48: ("David Arkenstone", "Papillon (On The Wings Of The Butterfly)", "New Age"),
49: ("David Arkenstone", "Stepping Stars", "New Age"),
50: ("David Arkenstone", "Carnation Lily Lily Rose", "New Age"),
51: ("David Lanz", "Behind The Waterfall", "New Age"),
52: ("David Lanz", "Cristofori's Dream", "New Age"),
53: ("David Lanz", "Heartsounds", "New Age"),
54: ("David Lanz", "Leaves on the Seine", "New Age"),
}

musicdata = sorted(musicdata.items())
musicdata = [[str(k)] + list(v) for k,v in musicdata]

class MyPanel(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.dvlc = dvlc = dv.DataViewListCtrl(self)
        
        # Give it some columns.
        # The ID col we'll customize a bit:
        dvlc.AppendTextColumn('id', width=40)
        dvlc.AppendTextColumn('artist', width=170)
        dvlc.AppendTextColumn('title', width=260)
        dvlc.AppendTextColumn('genre', width=80)
    
        # Load the data. Each item (row) is added as a sequence of values
        # whose order matches the columns
        for itemvalues in musicdata:
            dvlc.AppendItem(itemvalues)
    
        # Set the layout so the listctrl fills the panel
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(dvlc, 1, wx.EXPAND)
        
class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(None, 
                         title='DVC ListCtrl Demo Extraction')
        panel = MyPanel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()