from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.core.hawkapi import hawkapi
from hawkAPI.lib.core.hawklib import hawklib
from hawkAPI.lib.plugins.hawkXLSX import hawkXLSX
from datetime import datetime
from operator import itemgetter
import inspect
import sys

hawk = hawkcore("ipserver")
#hawk.setRetry(10)
hawk.login("user","pass")
#hawk.debug()
res = hawkapi(hawk)
lib = hawklib(hawk)
start = lib.getDateUtc('h',delta=24)
end = lib.getDateUtc()
dates = lib.getDates(str(start),str(end))
group = "groupname"
c = []
for i in dates:
    print "%s:%s --- %s" %(nstart,nend,idit)
    f = res.searchResAddrByGroup(nstart,nend,ip,group)
    if not f:
       pass
    else:
       for i in f:
           c.append(i)
c.sort(key=itemgetter('date_added'))
book = hawkXLSX("filename.xlsx",hawk)
keys = ["date_added","resource_addr","payload"]
book.build(c,nkeys=keys)
#book.build(c)
hawk.logout()
