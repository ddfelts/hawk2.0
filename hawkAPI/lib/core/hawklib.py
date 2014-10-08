import os
from datetime import datetime, timedelta


class hawklib():

        def __init__(self,hawk):
           self.hawk = hawk

	def getDateLocal(self,dtype="d",delta=0):
           if delta < 1:
              t = datetime.now()
              return t.replace(microsecond=0)
           else:
              data = int(delta)
              dtype = dtype.lower()
              if dtype == "d":
                 t = datetime.now() - timedelta(days = data)
                 return t.replace(microsecond=0)
              elif dtype == "h":
                 t = datetime.now() - timedelta(hours = data)
                 return t.replace(microsecond=0)
              elif dtype == "m":
                 t = datetime.now() - timedelta(minutes = data)
                 return t.replace(microsecond=0)
              elif dtype == "s":
                 t = datetime.now() - timedelta(seconds = data)
                 return t.replace(microsecond=0)
              else:
                self.hawk.callError('Wrong value for dtype in getDateLocal expected m or d or h or s',str(dtype))
                sys.exit(1)

	def getDateUtc(self,dtype="d",delta=0):
           if delta < 1:
              t = datetime.utcnow()
              return t.replace(microsecond=0)
           else:
              data = int(delta)
              dtype = dtype.lower()
              if dtype == "d":
                 t = datetime.utcnow() - timedelta(days = data)
                 return t.replace(microsecond=0)
              elif dtype == "h":
                 t = datetime.utcnow() - timedelta(hours = data)
                 return t.replace(microsecond=0)
              elif dtype == "m":
                 t = datetime.utcnow() - timedelta(minutes = data)
                 return t.replace(microsecond=0)
              elif dtype == "s":
                 t = datetime.utcnow() - timedelta(seconds = data)
                 return t.replace(microsecond=0)
              else:
                self.hawk.callError('Wrong value for dtype in getDateUtc expected m or d or h or s',str(dtype))
                sys.exit(1)

        def conDateToUtc(self,date):
              UTCOFF = datetime.utcnow() - datetime.now()
              ndate = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
              t = ndate + UTCOFF
              f = t.replace(microsecond=0)
              return f.strftime("%Y-%m-%d %H:%M:%S")

	def conDateToLocal(self,date):
            UTCOFF = datetime.utcnow() - datetime.now()
            ndate = datetime.strptime(date,"%Y-%m-%d %H:%M:%S.%f")
            t = ndate - UTCOFF
            f = t.replace(microsecond=0)
            return f.strftime("%Y-%m-%d %H:%M:%S")

	def getDates(self,start,end):
    	      nstart = datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
              nend = datetime.strptime(end,"%Y-%m-%d %H:%M:%S")
              d = nend - nstart
              totals = d.total_seconds()
              if int(totals) < 300:
                 return [start,end,0]
              tm = int(totals) / 60
              startdate = int(tm) / 5
              mydate = 0
              dates = []
              idit = 0
              for i in range(1,int(startdate)):
                  if mydate != 1:
                     nstart =  nend - timedelta(minutes=tm)
                     fend = nstart + timedelta(minutes=5)
                     dates.append([nstart,fend,idit])         
                     nstart = fend
                     mydate = 1
                  else:
                     idit = i
                     start = nstart
                     end = nstart + timedelta(minutes=5)
                     dates.append([start,end,idit])
                     nstart = end
              return dates

	def getKeys(self,data):
             all = []
             for i in data:
                for f in i.keys():
                    if f in all:
                       pass
                    else:
                       all.append(f)
             return all

	def print_table(self,rows):
          widths = [ len(max(columns, key=len)) for columns in zip(*rows) ]
          header, data = rows[0], rows[1:]
          print(
                ' | '.join( format(title, "%ds" % width) for width, title in zip(widths, header) )
          )
          print( '-+-'.join( '-' * width for width in widths ) )
          for row in data:
             print(
                   " | ".join( format(cdata, "%ds" % width) for width, cdata in zip(widths, row) )
             )


