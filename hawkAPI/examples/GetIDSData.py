from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.core.hawkapi import hawkapi
from hawkAPI.lib.core.hawklib import hawklib
from hawkAPI.lib.plugins.hawkXLSX import hawkXLSX
from datetime import datetime
from Queue import Queue
from threading import Thread
from pymongo import *
import sys

def dostuff(q,h,mq,group):
  while True:
       bstart,bend,idit = q.get()
       print "%s-%s ---%s" % ( bstart,bend,idit)
       mdata = h.getAlertsByGroup(bstart,bend,group,ct="IDS")
       if not mdata:
           q.task_done()       
       else:
         for b in mdata:
           if b["ip_src"] == None:
              src = "None"
           else:
              src = b["ip_src"]
           if b["ip_dst"] == None:
              dst = "None"
           else:
              dst = b["ip_dst"]
           if "payload" == None:
              payload = "None"
           else:
              payload = b["payload"]
           if "ip_sport" in b:
              if b["ip_sport"] == None :
                 ip_sport = "None"
              else:
                 ip_sport = b["ip_sport"]
           else:
              ip_sport = "None"
           if "ip_dport" in b:
              if b["ip_dport"] == None:
                 ip_dport = "None"
              else:
                 ip_dport = b["ip_dport"]
           else:
              ip_dport = "None"
           mq.put([b["date_added"],src,dst,b["alert_name"],payload,b["priority"],ip_sport,ip_dport])
         q.task_done()


def adddb(mq,col):
    while True:
          date,src,dst,alert_name,payload,priority,ip_sport,ip_dport = mq.get()    
          data = {"date":date,
                  "src":src,
                  "dst":dst,
                  "ipsport":ip_sport,
                  "ipdport":ip_dport,
                  "an":alert_name,
                  "pl":payload}

          col.insert(data)
          mq.task_done()

if __name__ == '__main__':

     import argparse
     usage = 'GetIDSData -u "id" -p "pass" -i "server" -c "client" -d days'
     parser = argparse.ArgumentParser(description="Pulls out IDS data for processing",epilog=usage)
     parser.add_argument("-u","--user",help="Username",type=str,required=True)
     parser.add_argument("-p","--passw",help="Password",type=str,required=True)
     parser.add_argument("-i","--server",help="The hawk server IP",type=str,required=True)
     parser.add_argument("-c","--client",help="Client name",type=str,required=True)
     parser.add_argument("-d","--days",help="Number of Days",type=int,required=True)

     opt = parser.parse_args()
     if len(sys.argv) < 5:
         parser.print_help()
         sys.exit()

     hawk = hawkcore(opt.server)
     hawk.login(opt.user,opt.passw)
     client = MongoClient('localhost', 27017)
     db = client["%s" % opt.client]
     col = db.alerts

     res = hawkapi(hawk)
     lib = hawklib(hawk)
     start = lib.getDateLocal(dtype="d",delta=opt.days).strftime("%Y-%m-%d")
     end = lib.getDateLocal().strftime("%Y-%m-%d")
     nend = str(start) + " 23:59:59"
     nstart = str(start) + " 00:00:00"
     alldates = lib.getDates(nstart,nend)

     myque = Queue()
     mainque = Queue()
     for i in alldates:
         myque.put(i)

     maxth = 10
     for i in range(maxth):
       work = Thread(target=dostuff, args=(myque,res,mainque,opt.client))
       work.setDaemon(True)
       work.start()

     for i in range(maxth):
       threadit = Thread(target=adddb,args=(mainque,col,))
       threadit.setDaemon(True)
       threadit.start()


     myque.join()
     mainque.join()
     hawk.logout()
     sys.exit(1)
