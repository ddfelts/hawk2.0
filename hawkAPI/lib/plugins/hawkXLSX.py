from hawkAPI.lib.core.hawklib import hawklib
import xlsxwriter

class hawkXLSX():

        def __init__(self,fn,hawk):

            self.wk = xlsxwriter.Workbook(fn)
            #self.ws = self.wk.add_worksheet()
            self.bold = self.wk.add_format({'bold':True,'border':1,'align':'center'})
            self.hlib = hawklib(hawk)

        def addpage(self,name,data,nkeys=None):
            ws = self.wk.add_worksheet(name) 
            if not nkeys:
               keys = self.hlib.getKeys(data)
            else:
               keys = nkeys 
            col=0
            for x in keys:
                ws.write(0,col,str(x),self.bold)
                col+=1
            row=1
            col=0
            for x in data:
                 for b in range(len(keys)):
                     if keys[b] not in x:
                        outb = None
                     else:
                        outb = x[keys[b]]
                     ws.write(row,col,str(outb))
                     col+=1
                 row+=1
                 col=0

        def close(self):
            self.wk.close()
