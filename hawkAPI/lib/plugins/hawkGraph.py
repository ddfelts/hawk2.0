import pygal
from pygal.colors import darken,lighten
from pygal.style import  Style
import tempfile
import os
import shutil

class hawkGraph:

	def __init__(self):
            mystyle = Style(
               #background=darken('#f8f8f8', 3),
               background='white',
               plot_background='white',
               foreground='rgba(0, 0, 0, 0.9)',
               foreground_light='rgba(0, 0, 0, 0.9)',
               foreground_dark='rgba(0, 0, 0, 0.6)',
               opacity='.5',
               opacity_hover='.9',
               transition='250ms ease-in',
               colors=('#00b2f0', '#43d9be', '#0662ab', 
                        darken('#00b2f0', 20),lighten('#43d9be', 20), 
                        lighten('#7dcf30', 10), darken('#0662ab', 15),
                        '#ffd541', '#7dcf30', lighten('#00b2f0', 15), darken('#ffd541', 20))
               )

            self.tmpDir = tempfile.mkdtemp()
            self.config = pygal.Config(style=mystyle,
                                      legend_font_size=10,
                                      width=500,height=250) 

        def getDir(self):
            return self.tmpDir

        def removeDir(self):
            try:
              shutil.rmtree(self.tmpDir)
            except:
              return 0
            return 1
                
        def HBar(self,title,data):             
            chart = pygal.HorizontalBar(self.config)
            chart.title = "" 
            for i in data:
                  chart.add(i['title'],i['data'])
            chart.render_to_png("%s/%s.png" % (self.tmpDir,title))

        def Pie(self,title,data):
            chart = pygal.Pie(self.config)
            chart.title = ""
            for i in data:
                  chart.add(i['title'],i['data'])
            chart.render_to_png("%s/%s.png" % (self.tmpDir,title))

