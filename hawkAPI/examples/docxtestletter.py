from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.core.hawkapi import hawkapi
from hawkAPI.lib.core.hawklib import hawklib
from hawkAPI.lib.plugins.hawkDOCX import hawkDOCX
from datetime import datetime
from operator import itemgetter


hawk = hawkcore("ipserver")
hawk.login("user","passw")
#hawk.debug()
res = hawkapi(hawk)
lib = hawklib(hawk)
#start = lib.getDateUtc('h',delta=24)
#end = lib.getDateUtc()
start = "2014-09-28 00:00:00"
end = "2014-09-28 01:00:00"
dates = lib.getDates(str(start),str(end))
group = "groupname"
c = []
#sn = datetime.now()
for i in dates:
    nstart,nend,idit = i
    print "%s:%s --- %s" %(nstart,nend,idit)
    f = res.getIDSAlertsByGroup(nstart,nend,group)
    if not f:
       pass
    else:
       for i in f:
           c.append(i)
c.sort(key=itemgetter('date_added'))
page = hawkDOCX("payload.docx","normal.docx",hawk)
keys = ["date_added","ip_src","ip_dst","payload"]
page.addTable(c,nkeys=keys)
page.saveDoc()
hawk.logout()
