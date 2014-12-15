import requests
import sys
import json
import logging
import httplib
import time
from socket import error as SocketError
import errno
from contextlib import closing
import re
import random

class hawkcore(object):

      def __init__(self,server):
         self.allsessions = []
         #self.sess = requests.session()
         self.server = server
         for i in self.server:
             data = {"server":i,"sess":requests.session()}
             self.allsessions.append(data)
             data = ""

         self.debugit = "False"
         self.retry = 0
         self.setretry = 5
         self.nd = []
         logging.getLogger("requests").setLevel(logging.CRITICAL)
         logging.getLogger("urllib3").setLevel(logging.CRITICAL)

      def reSession(self):
          self.sess = requests.session()

      def setCred(self,user,passw):
          self.user = user
          self.passw = passw

      def setRetry(self,retry):
          self.setretry = retry

      def logit(self,level,message,fout=None):
          logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',level=logging.DEBUG)
          if fout != None:
             logging.basicConfig(filename=fout,level=logging.DEBUG)
          if level == "DEBUG":
             logging.debug(message)
     	  if level == "INFO":
	         logging.info(message)
          if level == "WARNING":
             logging.warning(message)
          if level == "ERROR":
             logging.error(message)
          if level == "CRITICAL":
             logging.critical(message)

      def debug(self,level=1):
         httplib.HTTPConnection.debuglevel = level 
         logging.basicConfig()
         logging.getLogger().setLevel(logging.DEBUG)
         requests_log = logging.getLogger("requests.packages.urllib3")
         requests_log.setLevel(logging.DEBUG)
         requests_log.propagate = True
         self.debugit = "True"

      def login(self,user,passw):
         self.setCred(user,passw)
         data = {"username":user,"password":passw,"secure":"false"}
         try:
              for i in self.allsessions:
                  url = "https://%s:8080/API/1.1/login" % i["server"]
                  i["sess"].post(url,data,verify=False,allow_redirects=True)
         except requests.exceptions.ConnectionError:
              print "Connection Error during login"
              sys.exit(1)
         except requests.exceptions.Timeout:
              print "Timeout during login"
              sys.exit(1)    

      def logout(self):
          for i in self.allsessions:
              url = "https://%s:8080/API/1.1/logout" % i["server"]
              r = i["sess"].get(url,verify=False) 
          return "true"

      def callError(self,a,b):
          raise Exception(a,b)
          #sys.exit(1) 
 
      def checkData(self,data):
          if "status" in data:
              if data["status"] == "success":
                 return data["results"]
              if data["status"] == "failure":
                  if data["details"] == "Invalid session, unable to continue.":
                     print 'Hawk Failure: geting new session'
                     self.debug()
                     self.reSession()
                     self.login(self.user,self.passw)
                  return 0
          else:
              return 0


      def doGet(self,data):
         url = "https://%s:8080/API/1.1/%s" % (self.server,data)
         try:
             r = self.sess.get(url,verify=False,stream=True,allow_redirects=True)
             if r.status_code == requests.codes.ok:
                 pass
             else:
                 print "Proper code not returned %s" % r.status_code
                 self.logout()
                 sys.exit(1)
             ndata = ""
             ndata = r.json()
             if self.debugit == "True":
                 print ndata
                 return ndata
             else:
                 return ndata
         except requests.exceptions.Timeout:
             self.doGet(data)
         except SocketError as e:
             if e.errno == errno.ECONNRESET:
                 self.doGet(data)


      def doPost(self,api,data={}):
          if self.retry < self.setretry:
             bdata = self.doTest(api,data)
             if bdata != 0:
                 self.retry = 0.
                 return bdata
             else:
                 time.sleep(3)
                 self.retry += 1
                 self.doPost(api,data)
          else:
              print "Failed %s retrys" % str(self.retry)
              sys.exit(1)
 
      def newdata(self,data):
          self.nd.append(data)

      def getnewdata(self):
          return self.nd

      def doTest(self,api,data={}):
         #url = "https://%s:8080/API/1.1/%s" % (self.server,api)
         try:
             i = random.choice(self.allsessions)
             url = "https://%s:8080/API/1.1/%s" % (i["server"],api)
             with closing(i["sess"].post(url,data,verify=False,stream=True,allow_redirects=True)) as r:
               if r.status_code == requests.codes.ok:
                   pass
               else:
                   print "Proper code not returned %s doing retry" % r.status_code
                   return 0
               data ="" 
               if self.debugit == "True":
                   print r.text
               for i in r.iter_content(chunk_size=1046):
                   data += i
               try:
                  ndata = json.loads(data)
               except requests.exceptions.RequestException as e:
                  return 0
               #ndata = r.json()
               if len(ndata) > 1:
                  if self.debugit == "True":
                     print ndata
                     return self.checkData(ndata)
                  else:
                     return self.checkData(ndata)
               else:
                   return 0
         except requests.exceptions.Timeout:
                self.doTest(api,data)
         except SocketError as e:
                if e.errno == errno.ECONNRESET:
                   self.doTest(data)

      def getDevices(self,data={}):
         url = "search/resource" 
         ndata = self.doPost(url,data)
         return ndata

      def getShardStats(self):
          url = "shards/stats"
          data = self.doGet(url)
          return self.checkData(data)

      def getAudit(self,data={}):
          api = "search/audit"
          ndata = self.doPost(api,data)
          return ndata

      def getShardLists(self):
          url = "shards/list"
          data = self.doGet(url)
          return self.checkData(data)         


      def traverse(self,o):
          res = []
          for b in o:
            if b["children"] == False:
              res.append(b["key"])
            else:
              res.append(b["key"])
              res.extend(self.traverse(b["children"]))
          return res

      def getGroups(self,data):
          if data == None:
             url = "group"
          else:
             url = "group?%s" % data
          ndata = self.doGet(url)
          ndata = self.checkData(ndata)
          if not ndata:
              return 0
          else:
              fdata = self.traverse(ndata["children"])
              if data == None:
                  return fdata
              else:
                  fdata.append(data[5:])
                  return fdata


      def getEvents(self,data):
         api = "search/events"
         ndata = self.doPost(api,data)
         return ndata

      def getIncidents(self,data={}):
          api = "search/incidents"
          ndata = self.doPost(api,data)
          return ndata

      def getVulns(self,data={}):
          api = "search/vulnerabilities"
          ndata = self.doPost(api,data)
          return ndata

      def getUsers(self,data={}):
          api = "search/users"
          ndata = self.doPost(api,data)
          return ndata

