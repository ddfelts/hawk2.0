from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.core.hawkapi import hawkapi
from hawkAPI.lib.core.hawklib import hawklib
from hawkAPI.lib.plugins.hawkPDF import hawkPDF
from datetime import datetime
from operator import itemgetter
import inspect
import sys


hawk = hawkcore("ipserver")
hawk.setRetry(10)
hawk.login("user","passwrd")
#hawk.debug()
res = hawkapi(hawk)
lib = hawklib(hawk)
start = "2014-10-04 13:00:0"
end = "2014-10-04 14:00:00"
dates = lib.getDates(str(start),str(end))
group = "groupname"
c = []
for i in dates:
    nstart,nend,idit = i
    print "%s:%s --- %s" %(nstart,nend,idit)
    f = res.getAlertsByGroup(nstart,nend,group)
    if not f:
       pass
    else:
       for i in f:
           c.append(i)

c.sort(key=itemgetter('date_added'))
book = hawkPDF("tester.pdf",hawk)
book.setTitle("Test PDF")
book.setDate(start,end)
book.setClientName(group)
book.setClientImage("/home/ddfelts/images.jpeg")
book.addPageBreak()
book.setPageLandscape()
book.addStoryTitle("Top Ten IP Sources")
book.addStory("Top ten IP sources outlines the top ten source IP addresses creating alerts.")
keys = ["date_added","ip_src","ip_dst","resource_addr","alert_name"]
book.addTable(c,keys)
book.savePdf()
hawk.logout()
