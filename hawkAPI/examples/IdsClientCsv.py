#!/usr/bin/python
import sys
import os
import string
from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.plugins.hawkGraph import hawkGraph
from hawkAPI.lib.plugins.hawkXLSX import hawkXLSX
import argparse
from pymongo import *
from bson.son import SON

usage = 'IdsClientcsv -c client -l dir'
parser = argparse.ArgumentParser(description="PDF output by client for IDS alerts",epilog=usage)
parser.add_argument("-l","--dir",help="location to store",type=str,required=True)
parser.add_argument("-c","--client",help="client",type=str,required=True)

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit()
opt = parser.parse_args()

hawk = hawkcore([None])
client = MongoClient('localhost', 27017)
db = client["%s" % opt.client]
col = db.alerts
col.create_index([("date",DESCENDING)])
srcs = col.find().sort('date')
fin = []
for i in srcs:
    tax = {"date":i["date"],
           "ip_src":i["src"],
           "ip_sport":i["ipsport"],
           "ip_dst":i["dst"],
           "ip_dport":i["ipdport"],
           "alert_name":i["an"],
           "priority":i["pri"]}
    fin.append(tax)
    tax=""
alldata = fin
keys = ["date","priority","ip_src","ip_sport","ip_dst","ip_dport","alert_name"]
nameit = opt.dir + opt.client + "-ids.xlsx"
book = hawkXLSX(nameit,hawk)
book.addpage("idsdata",alldata,nkeys=keys)
book.close()
sys.exit(1)
