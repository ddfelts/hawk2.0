from hawkAPI.lib.core.hawklib import hawklib
import csv 

class hawkCSV():

        def __init__(self,fn,hawk):

            self.n = open(fn,'w')
            self.w = csv.writer(self.n,delimiter = ",")
            self.hlib = hawklib(hawk)

        def build(self,data,nkeys=None):
            
            if not nkeys:
               keys = self.hlib.getKeys(data)
            else:
               keys = nkeys 
            self.w.writerow(keys)
            for x in data:
                 fdata = []
                 for b in range(len(keys)):
                     if keys[b] not in x:
                        outb = None
                     else:
                        outb = x[keys[b]]
                     fdata.append(str(outb))
                 self.w.writerow(fdata)
            self.n.close()
