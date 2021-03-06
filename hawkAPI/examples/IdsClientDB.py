#!/usr/bin/python
import sys
import os
import string
from hawkAPI.lib.core.hawkcore import hawkcore 
from hawkAPI.lib.plugins.hawkGraph import hawkGraph
from hawkAPI.lib.plugins.hawkPDF import hawkPDF
import argparse
from pymongo import *
from bson.son import SON

usage = 'IdsClientDB -c client -l dir -o -a -b'
parser = argparse.ArgumentParser(description="PDF output by client for IDS alerts",epilog=usage)
parser.add_argument("-l","--dir",help="location to store",type=str,required=True)
parser.add_argument("-o","--logo",help="path to logo",type=str,required=False)
parser.add_argument("-a","--plogo",help="path to page logo",type=str,required=False)
parser.add_argument("-b","--alerts",help="Add all alerts",action="store_true",required=False)
parser.add_argument("-c","--client",help="client",type=str,required=True)

if len(sys.argv) < 3:
    parser.print_help()
    sys.exit()
opt = parser.parse_args()

hawk = hawkcore(None)
graph = hawkGraph()
client = MongoClient('localhost', 27017)
db = client["%s" % opt.client]
col = db.alerts


start = col.find_one()
nstart = start["date"]
nstart = nstart[0:10] + " 00:00:00"
end = col.find().sort('date',-1).limit(1)
for i in end:
    nend = i["date"]
fend = nend[0:10] + " 23:55:55"

col.create_index([("src",DESCENDING)])
pipe = [{"$group":{"_id":"$src","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":10}]
srcs = col.aggregate(pipe)
main = []
fin = []
for i in srcs["result"]:
    main.append({"title":i["_id"],
                 "data":int(i["count"])})   
    tax = {"ip_src":i["_id"],
           "ip_src_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.HBar("Top_IP_Source",main)
ipdata = fin

pipe = [{"$group":{"_id":"$dst","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":10}]
srcs = col.aggregate(pipe)
main = []
fin = []

for i in srcs["result"]:
    main.append({"title":i["_id"],
                 "data":int(i["count"])})   
    tax = {"ip_dst":i["_id"],
           "ip_dst_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.Pie("Top_IP_Dst",main)
dstdata = fin

pipe = [{"$group":{"_id":"$an","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":10}]
srcs = col.aggregate(pipe)
#Get Top alerts by group name
main = []
fin = []
for i in srcs["result"]:
    main.append({"title":i["_id"],
                 "data":i["count"]})   
    tax = {"alert_name":i["_id"],
           "alert_name_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.HBar("Top_Ten_Alerts",main)
adata = fin

pipe = [{"$group":{"_id":"$pri","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":5}]
srcs = col.aggregate(pipe)
main = []
fin = []
for i in srcs["result"]:
    main.append({"title":str(i["_id"]),
                 "data":i["count"]})   
    tax = {"priority":i["_id"],
           "priority_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.HBar("Top_5_Priority",main)
pdata = fin


pipe = [{"$group":{"_id":"$ipsport","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":5}]
srcs = col.aggregate(pipe)
main = []
fin = []
for i in srcs["result"]:
    main.append({"title":str(i["_id"]),
                 "data":i["count"]})   
    tax = {"ip_sport":i["_id"],
           "ip_sport_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.HBar("Top_10_SrcPort",main)
sportdata = fin


pipe = [{"$group":{"_id":"$ipdport","count":{"$sum":1}}},
        {"$sort":SON([("count",-1),("_id",-1)])},
        {"$limit":5}]
srcs = col.aggregate(pipe)
main = []
fin = []
for i in srcs["result"]:
    main.append({"title":str(i["_id"]),
                 "data":i["count"]})   
    tax = {"ip_dport":i["_id"],
           "ip_dport_count":i["count"]}
    fin.append(tax)
    tax = ""
graph.HBar("Top_10_DstPort",main)
dportdata = fin

srcs = col.find()
main = []
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

nameit = opt.dir + opt.client + "-ids.pdf"
doc = hawkPDF(nameit)
doc.setTitle("IDS Report")
doc.setDates(str(nstart),str(fend))
doc.setClient(opt.client)
if opt.logo:
   doc.setCImage(opt.logo)
if opt.plogo:
   doc.setPImage(opt.plogo)


doc.setPortrait()
doc.addStoryTitle("Top Ten IP Sources")
doc.addStory("Top ten IP sources outlines the top ten source IP addresses creating alerts.")
doc.addImage("%s/Top_IP_Source.png" % graph.getDir(),450,200)
keys = ["ip_src","ip_src_count"]
doc.addTable(ipdata,nkeys=keys)
doc.addPageBreak()

doc.addStoryTitle("Top 10 IP Source Port")
doc.addStory("This information displays the top 10 source ports.")
doc.addImage("%s/Top_10_SrcPort.png" % graph.getDir(),450,200)
keys = ["ip_sport","ip_sport_count"]
doc.addTable(sportdata,nkeys=keys)
doc.addPageBreak()

doc.addStoryTitle("Top Ten Destinations")
doc.addStory("Top ten IP destination outlines the top ten targets being attacked or causing alerts on the network.")
doc.addImage("%s/Top_IP_Dst.png" % graph.getDir(),450,200)
keys = ["ip_dst","ip_dst_count"]
doc.addTable(dstdata,nkeys=keys)
doc.addPageBreak()

doc.addStoryTitle("Top 10 IP Destination Port")
doc.addStory("This information displays the top 10 destination ports.")
doc.addImage("%s/Top_10_DstPort.png" % graph.getDir(),450,200)
keys = ["ip_dport","ip_dport_count"]
doc.addTable(dportdata,nkeys=keys)
doc.addPageBreak()

doc.addStoryTitle("Top Ten Alerts")
doc.addStory("This information displays the top ten alerts that are present and that have been seen in the current enviroment")
doc.addImage("%s/Top_Ten_Alerts.png" % graph.getDir(),450,200)
keys = ["alert_name","alert_name_count"]
doc.addTable(adata,nkeys=keys)
doc.addPageBreak()

doc.addStoryTitle("Top 5 Priorities")
doc.addStory("This information displays the priorities either set by hawk or Vendor Defaults (1 = High)")
doc.addImage("%s/Top_5_Priority.png" % graph.getDir(),450,200)
keys = ["priority","priority_count"]
doc.addTable(pdata,nkeys=keys)
doc.addPageBreak()

if opt.alerts:
   doc.addStoryTitle("Alerts By Date")
   doc.addStory("Below are Alerts Ordered by Date")
   keys = ["date","ip_src","ip_sport","ip_dst","ip_dport","alert_name","priority"]
   doc.addTable(alldata,nkeys=keys)
   doc.addPageBreak()

doc.savePDF()
graph.removeDir() 
sys.exit(1)
