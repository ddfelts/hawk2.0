import time
import sys
from reportlab.platypus import SimpleDocTemplate,LongTable,CondPageBreak,Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import utils
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Rect, Line
from reportlab.lib.colors import red, green, black, blue, lightblue
from reportlab.lib.pagesizes import letter, landscape
from hawkAPI.lib.core.hawklib import hawklib


class ReportDocument(SimpleDocTemplate):

      def __init__(self,pdfName,**kw):
          apply(SimpleDocTemplate.__init__, (self, pdfName), kw)

      def afterFlowable(self, flowable):  
         "Registers TOC entries."  
         if flowable.__class__.__name__ == 'Paragraph':  
             text = flowable.getPlainText()
             style =  flowable.style.name
             if style == "Heading1": 
                self.notify('TOCEntry', (0, text, self.page))  

class hawkPDF:

      def __init__(self,pdfName,hawk):
          #self.c = canvas.Canvas(pdfName)
          self.doc = ""
          self.docname = pdfName
          #ReportDocument(pdfName,showBoundary=1)
          #self.c = canvas.Canvas(pdfName)
          #self.PAGE_HEIGHT=defaultPageSize[1]
          #self.PAGE_WIDTH=defaultPageSize[0]
          self.story = []
          self.styles = getSampleStyleSheet()
          self.Title = ""
          self.startDate = ""
          self.endDate = ""
          self.client = ""
          self.image = ""
          self.cimage = ""
          self.hlib = hawklib(hawk)
          #self.lw,self.lh = letter
          self.pgtype = "letter"

      def setPageLetter(self):
             self.pgtype = "letter"
             self.lw,self.lh = letter
             self.doc = ReportDocument(self.docname,pagesize=(self.lw,self.lh))
             

      def setPageLandscape(self):
             self.pgtype = "landscape"
             self.lw,self.lh = landscape(letter)
             self.doc = ReportDocument(self.docname,pagesize=(self.lw,self.lh))

      def setTitle(self,title):
          self.Title = title

      def setClientName(self,name):
          self.client = name

      def get_aspect(self,path):
          img = utils.ImageReader(path)
          iw,ih = img.getSize()
          aspect = ih / float(iw)
          return aspect

      def get_im_size(self,path):
          img = utils.ImageReader(path)
          return img.getSize()

      def myFirstPage(self,canvas,doc):
          canvas.saveState()
          if self.pgtype == "landscape":
             #self.lw,self.lh = landscape
             #canvas.setPageSize((self.lw,self.lh))
             canvas.setFont("Times-Bold",30)
             canvas.drawString(1 * inch,6 * inch , self.Title)
             canvas.setFont("Times-Bold",14)
             canvas.drawString(1 * inch,5.75 * inch,"Start (%s) - End (%s)" % (self.startDate,self.endDate))
             canvas.drawString(1 * inch,5.55 * inch,"Client: %s" % self.client)
             if self.image != "":
                canvas.drawImage(self.image,self.lw/2.0,self.lh-168,width=150,height=50)
             canvas.restoreState()
          else:
             #canvas.setPageSize((self.lw,self.lh))
             canvas.setFont("Times-Bold",30)
             canvas.drawString(1 * inch,9 * inch , self.Title)
             canvas.setFont("Times-Bold",16)
             canvas.drawString(1 * inch,8.5 * inch,"Start (%s) - End (%s)" % (self.startDate,self.endDate))
             canvas.drawString(1 * inch,8.25 * inch,"Client: %s" % self.client)
             iw,ih = self.get_im_size(self.image)
             aspect = self.get_aspect(self.image)
             if self.image != "":
                canvas.drawImage(self.image,self.lw-150,self.lh-80,width=120,height=(120 * aspect))
             if self.cimage != "":
                canvas.drawImage(self.cimage,2.0625 * inch,self.lh-400,width=self.lw/2,height=(self.lw/2 * aspect))
             canvas.restoreState()

      def myLaterPage(self,canvas,doc):
          canvas.saveState()
          if self.pgtype == "landscape":
             #self.lw,self.lh = landscape
             #canvas.setPageSize((self.lw, self.lh))
             canvas.setFont("Times-Roman",10)
             canvas.drawString(9.25 * inch, self.lh - 25,"Client Name: %s " % (self.client))
             canvas.line(.50 * inch, self.lh - 50, 10.75 * inch,self.lh - 50)
             canvas.line(.50 * inch,1 * inch, 10.75 * inch,1 * inch)
             canvas.drawString(inch, 0.75 * inch, "Page: %d" % (doc.page))
             canvas.restoreState()
          else:
             #canvas.setPageSize((self.lw,self.lh))
             canvas.setFont("Times-Roman",10)
             canvas.drawString(6.25 * inch, self.lh - 25,"Client Name: %s " % (self.client))
             canvas.line(.50 * inch, self.lh - 50, 8 * inch, self.lh - 50)
             canvas.line(.50 * inch,1 * inch, 8 * inch,1 * inch)
             canvas.drawString(inch, 0.75 * inch, "Page: %d" % (doc.page))
             canvas.restoreState()

      def setDate(self,start,end):
          self.startDate = start
          self.endDate = end

      def setPageImage(self,image):
          self.image = image

      def setClientImage(self,image):
          self.cimage = image

      def createToc(self):
          centered = PS(name = 'centered',  
                        fontSize = 30,  
                        leading = 16,  
                        alignment = 1,  
                        spaceAfter = 20)
          self.story.append(Paragraph('<b>Table of contents</b>',centered))
          toc = TableOfContents()
          self.story.append(toc)
          self.addPageBreak()

      def addStory(self,text):
          t = Paragraph(text,self.styles["Normal"])
          self.story.append(t)
          self.story.append(Spacer(1,12))

      def addStoryTitle(self,text):
          t = Paragraph(text,self.styles["Heading1"])
          self.story.append(t)
          self.story.append(Spacer(1,12))


      def addTable(self,ndata,nkeys=None):
          data = []
          if not nkeys:
             keys = self.hlib.getKeys(ndata)
             data.append(keys)
          else:
             keys = nkeys 
             data.append(nkeys)
          for x in ndata:
              lister = [] 
              for b in range(len(keys)):
                  if keys[b] not in x:
                     outb = None
                  else:
                     outb = x[keys[b]]
                  t = Paragraph(str(outb),self.styles["Normal"])
                  lister.append(t)
              data.append(lister)

          tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),black),
                                 ('VALIGN',(0,0),(-1,-1),'TOP'),
                                 ('BOX',(0,0),(-1,-1),1,black),
                                 ('INNERGRID',(0,0),(-1,-1),1,black),
                                 ('BACKGROUND',(0,0),(-1,0),lightblue)])

          t = LongTable(data,repeatRows=1)
          t.setStyle(tblStyle)
          self.story.append(t)
          self.story.append(CondPageBreak(6))

      def addImage(self,image,w,h):
          self.story.append(Image(image,w,h))
          self.story.append(Spacer(1,12))

      def addPageBreak(self):
          self.story.append(PageBreak())

      def savePdf(self):
          if self.doc == "":
             self.setPageLetter()
          self.doc.multiBuild(self.story,onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPage)
