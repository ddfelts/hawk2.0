
 
class hawkapi():      

      def __init__(self,hawk):
          self.hawk = hawk

      def getAllUsers(self):
              bdata = {"column[]":"uid"}
              return self.hawk.getUsers(ndata)

      def getAuditByUser(self,user,da=0,lm=0):
          ndata = {"column[0]":"audit_id",
                   "column[1]":"username",
                   "column[2]":"group",
                   "column[3]":"category",
                   "column[4]":"method",
                   "column[5]":"status",
                   "column[6]":"action",
                   "column[7]":"criteria",
                   "column[8]":"date_added",
                   "where[0]":"username = '%s'" % user}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if da != 0:
             ndata.update({"where[1]":"date_added = '%s'" % da})
          return self.hawk.getAudit(ndata)

      def getAuditByGroup(self,group,da=0,lm=0):
          ndata = {"column[0]":"audit_id",
                   "column[1]":"username",
                   "column[2]":"group",
                   "column[3]":"category",
                   "column[4]":"method",
                   "column[5]":"status",
                   "column[6]":"action",
                   "column[7]":"criteria",
                   "column[8]":"date_added",
                   "where[0]":"group = '%s'" % group}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if da != 0:
             ndata.update({"where[1]":"date_added = '%s'" % da})
          return self.hawk.getAudit(ndata)

      def getUsersByGroup(self,client):
          ndata = {"column[0]":"uid",
                   "column[1]":"username",
                   "column[2]":"email",
                   "column[3]":"fullname",
                   "column[4]":"timezone",
                   "column[5]":"email_recipient",
                   "column[6]":"account_lock",
                   "column[7]":"group_name",
                   "column[8]":"phone",
                   "column[9]":"phone2",
                   "column[10]":"signature",
                   "column[11]":"audit",
                   "column[12]":"log",
                   "column[13]":"search",
                   "column[14]":"event_manager",
                   "column[15]":"sysop",
                   "column[16]":"reports",
                   "column[17]":"filter_manager",
                   "column[18]":"moderator",
                   "column[19]":"admin",
                   "where[0]":"group_name = '%s'" % client}
          return self.hawk.getUsers(ndata)

      def getResByGroup(self,client,mtype=""):
          ndata = {"column[0]":"resource_name",
                   "where[0]":"resource_group = '%s'" % client}
          if mtype != "":
              ndata.update({"where[1]":"class_type = '%s'" % mtype})
          return self.hawk.getDevices(ndata)

      def getResTypeByGroup(self,client,mtype="IDS"):
          ndata = {"column[0]":"resource_name",
                   "where[0]":"resource_group = '%s'" % client,
                   "where[1]":"class_type = '%s'" % mtype}
          return self.hawk.getDevices(ndata)


      def getResType(self,mtype="IDS"):
          ndata = {"column[0]":"resource_name",
                   "column[1]":"class_type",
                   "where[1]":"class_type = '%s'" % mtype}
          data = self.hawk.getDevices(ndata)
          resource = []
          final = {"total":0,"resource":[]}
          for i in data:
               if  i["resource_name"] in resource:
                   pass
               else:
                   resource.append(i["resource_name"])
                   final["resource"].append(i)
                   final["total"] += 1
          return final

      def getRes(self,res=""):
          ndata ={"column[0]":"resource_name",
                  "where[0]":"resource_name = '%s'" % res}
          data = self.hawk.getDevices(ndata)
          return data

      def getTopGroups(self,start,end,lm=0):
          ndata = {"column[0]":"group_name",
                   "column[1]":"count group_name",
                   "group_by":"group_name",
                   "order_by":"group_name_count DESC",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopAlerts(self,start,end,lm=0):
          ndata = {"column[0]":"alert_name",
                   "column[1]":"count alert_name",
                   "column[2]":"group_name",
                   "group_by":"alert_name,group_name",
                   "order_by":"alert_name_count DESC",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopAlertsByGroup(self,start,end,client,lm=0):
          ndata = {"column[0]":"alert_name",
                   "column[1]":"count alert_name",
                   "group_by":"alert_name",
                   "order_by":"alert_name_count DESC",
                   "where[0]":"group_name = '%s'" % client,
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getAllPriority(self,start,end):
          ndata = {"column[0]":"priority",
                   "column[1]":"count priority",
                   "column[2]":"group_name",
                   "group_by":"priority,group_name",
                   "order_by":"priority_count DESC",
                   "begin":"%s" % start,
                   "end":"%s" % end,
                   "limit":"5"}
          return self.hawk.getEvents(ndata)

      def getAllPriorityByGroup(self,start,end,group,lm=0):
         ndata = {"column[0]":"priority",
                  "column[1]":"count priority",
                  "group_by":"priority",
                  "order_by":"priority_count DESC",
                  "where[0]":"group_name = '%s'" % group,
                  "begin":"%s" % start,
                  "end":"%s" % end}
         if lm != 0:
              ndata.update({"limit":"%s" % lm})
         return self.hawk.getEvents(ndata)
         
      def getAllIdsPriorityByGroup(self,start,end,group,lm=0):
         ndata = {"column[0]":"priority",
                  "column[1]":"count priority",
                  "group_by":"priority",
                  "order_by":"priority_count DESC",
                  "where[0]":"group_name = '%s'" % group,
                  "where[1]":"class_type = 'IDS'",
                  "begin":"%s" % start,
                  "end":"%s" % end}
         if lm != 0:
              ndata.update({"limit":"%s" % lm})
         return self.hawk.getEvents(ndata)


      def getTopIpSrc(self,start,end,lm=0):
             ndata = {"column[0]":"ip_src",
                      "column[1]":"count ip_src",
                      "column[2]":"group_name",
                      "group_by":"ip_src,group_name",
                      "order_by":"ip_src_count DESC",
                      "where[0]":"ip_src != '138.69.211.22'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopIpSrcByGroup(self,start,end,client,lm=0):
             ndata = {"column[0]":"ip_src",
                      "column[1]":"count ip_src",
                      "group_by":"ip_src",
                      "order_by":"ip_src_count DESC",
                      "where[0]":"group_name = '%s'" % client,
                      "where[1]":"ip_src != '138.69.211.22'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopIdsIpSrcByGroup(self,start,end,client,lm=0):
             ndata = {"column[0]":"ip_src",
                      "column[1]":"count ip_src",
                      "group_by":"ip_src",
                      "order_by":"ip_src_count DESC",
                      "where[0]":"group_name = '%s'" % client,
                      "where[1]":"ip_src != '138.69.211.22'",
                      "where[2]":"class_type = 'IDS'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopIpDst(self,start,end,lm=0):
             ndata = {"column[0]":"ip_dst",
                      "column[1]":"count ip_dst",
                      "column[2]":"group_name",
                      "group_by":"ip_dst,group_name",
                      "order_by":"ip_dst_count DESC",
                      "where[0]":"ip_dst != '138.69.211.22'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopIpDstByGroup(self,start,end,client,lm=0):
             ndata = {"column[0]":"ip_dst",
                      "column[1]":"count ip_dst",
                      "group_by":"ip_dst",
                      "order_by":"ip_dst_count DESC",
                      "where[0]":"group_name = '%s'" % client,
                      "where[1]":"ip_dst != '138.69.211.22'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopIdsIpDstByGroup(self,start,end,client,lm=0):
             ndata = {"column[0]":"ip_dst",
                      "column[1]":"count ip_dst",
                      "group_by":"ip_dst",
                      "order_by":"ip_dst_count DESC",
                      "where[0]":"group_name = '%s'" % client,
                      "where[1]":"ip_dst != '138.69.211.22'",
                      "where[2]":"class_type = 'IDS'",
                      "begin":"%s" % start,
                      "end":"%s" % end}
             if lm != 0:
                ndata.update({"limit":"%s" % lm})
             return self.hawk.getEvents(ndata)

      def getTopSrcCountry(self,start,end,lm=0):
          ndata = {"column[0]":"geoip_name ip_src",
                   "column[2]":"count ip_src_geoip_name",
                   "column[1]":"group_name",
                   "group_by":"ip_src_geoip_name,group_name",
                   "order_by":"ip_src_geoip_name_count DESC",
                   "where[0]":"ip_src_geoip_name != ''", 
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopSrcCountryByGroup(self,start,end,client,lm=0):
          ndata = {"column[0]":"geoip_name ip_src",
                   "column[2]":"count ip_src_geoip_name",
                   "group_by":"ip_src_geoip_name",
                   "order_by":"ip_src_geoip_name_count DESC", 
                   "where[0]":"group_name = '%s'" % client,
                   "where[1]":"ip_src_geiop_name != ''",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopDstCountry(self,start,end,lm=0):
          ndata = {"column[0]":"geoip_name ip_dst",
                   "column[2]":"count ip_dst_geoip_name",
                   "column[1]":"group_name",
                   "group_by":"ip_dst_geoip_name,group_name",
                   "order_by":"ip_dst_geoip_name_count DESC",
                   "where[0]":"ip_dst_geoip_name != ''", 
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopDstCountryByGroup(self,start,end,client,lm=0):
          ndata = {"column[0]":"geoip_name ip_dst",
                   "column[2]":"count ip_dst_geoip_name",
                   "group_by":"ip_dst_geoip_name",
                   "order_by":"ip_dst_geoip_name_count DESC", 
                   "where[0]":"group_name = '%s'" % client,
                   "where[1]":"ip_dst_geoip_name != ''",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getAllRes(self):
          ndata = {"column[]":"resource_name"}
          return self.hawk.getDevices(ndata)

      def getTopRes(self,start,end,lm=0):
          ndata = {"column[0]":"resource_name",
                   "column[1]":"count resource_name",
                   "column[2]":"group_name",
                   "group_by":"resource_name,group_name",
                   "order_by":"resource_name_count DESC",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)

      def getTopResByGroup(self,start,end,client,lm=0):
          ndata = {"column[0]":"resource_name",
                   "column[1]":"count resource_name",
                   "group_by":"resource_name",
                   "order_by":"resource_name_count DESC",
                   "where[0]":"group_name = '%s'" % client,
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          return self.hawk.getEvents(ndata)    
      
      def getIDSAlerts(self,start,end,lm=0,res=""):
          ndata = {"column[1]":"date_added",
                   "column[2]":"ip_src",
                   "column[3]":"ip_dst",
                   "column[4]":"alert_name",
                   "column[5]":"group_name",
                   "column[6]":"geoip_name ip_src",
                   "column[7]":"geoip_name ip_dst",
                   "order_by":"date_added",
                   "where[0]":"class_type = 'IDS'",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          if res != "":
              ndata.update({"where[1]":"resource_name = '%s'" % res})
          return self.hawk.getEvents(ndata)

      def getIDSAlertsByGroup(self,start,end,group,lm=0,res=""):
          ndata = {"column[1]":"date_added",
                   "column[2]":"ip_src",
                   "column[3]":"ip_dst",
                   "column[4]":"alert_name",
                   "column[5]":"group_name",
                   "column[6]":"geoip_name ip_src",
                   "column[7]":"geoip_name ip_dst",
                   #"order_by":"date_added",
                   "where[0]":"class_type = 'IDS'",
                   "where[1]":"group_name = '%s'" % group,
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          if res != "":
              ndata.update({"where[2]":"resource_name = '%s'" % res})
          return self.hawk.getEvents(ndata)

      def getTopIdsAlertsByGroup(self,start,end,group,lm=0,res=""):
           ndata = {"column[1]":"date_added",
                    "column[2]":"ip_src",
                    "column[3]":"ip_dst",
                    "column[4]":"alert_name",
                    "column[5]":"group_name",
                    "column[6]":"count alert_name",
                    "order_by":"alert_name_count DESC",
                    "group_by":"alert_name",
                    "where[0]":"class_type = 'IDS'",
                    "where[1]":"group_name = '%s'" % group,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           if res != "":
              ndata.update({"where[2]":"resource_name = '%s'" % res})
           return self.hawk.getEvents(ndata)

      def getAlerts(self,start,end,lm=0,ct="",an=""):
          ndata = {"column[1]":"date_added",
                   "column[2]":"ip_src",
                   "column[3]":"ip_dst",
                   "column[4]":"alert_name",
                   "column[5]":"group_name",
                   "column[6]":"geoip_name ip_src",
                   "column[7]":"geoip_name ip_dst",
                   #"order_by":"date_added",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[0]":"class_type = '%s'" % ct})
          if an != "":
             ndata.update({"where[1]":"alert_name = '%s'" % an})
          return self.hawk.getEvents(ndata)

      def getAlertsByGroup(self,start,end,group,lm=0,ct="",an=""):
          ndata = {"column[1]":"date_added",
                   "column[2]":"ip_src",
                   "column[3]":"ip_dst",
                   "column[4]":"alert_name",
                   "column[8]":"payload",
                   "column[5]":"group_name",
                   "column[6]":"geoip_name ip_src",
                   "column[7]":"geoip_name ip_dst",
                   #"order_by":"date_added",
                   "where[0]":"group_name = '%s'" % group,
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
              ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[1]":"class_type = '%s'" % ct})
          if an != "":
              ndata.update({"where[2]":"alert_name = '%s'" % an})
          return self.hawk.getEvents(ndata)


      def getLowAlerts(self,start,end,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"name",
                   "column[7]":"alerts_type_name",
                   "order_by":"date_added",
                   "where[1]":"priority = (3 or 4 or 5)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[0]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def getUsersByGroup(self,client):
          ndata = {"column[0]":"uid",
                   "column[1]":"username",
                   "column[2]":"email",
                   "column[3]":"fullname",
                   "column[4]":"timezone",
                   "column[5]":"email_recipient",
                   "column[6]":"account_lock",
                   "column[7]":"group_name",
                   "column[8]":"phone",
                   "column[9]":"phone2",
                   "column[10]":"signature",
                   "column[11]":"audit",
                   "column[12]":"log",
                   "column[13]":"search",
                   "column[14]":"event_manager",
                   "column[15]":"sysop",
                   "column[16]":"reports",
                   "column[17]":"filter_manager",
                   "column[18]":"moderator",
                   "column[19]":"admin",
                   "where[0]":"group_name = '%s'" % client}
          return self.hawk.getUsers(ndata)



      def getLowAlertsByGroup(self,start,end,client,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"name",
                   "column[7]":"alerts_type_name",
                   #"order_by":"date_added",
                   "where[0]":"group_name = '%s'" % client,
                   "where[1]":"priority = (3 or 4 or 5)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[2]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def getMedAlerts(self,start,end,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"name",
                   "column[7]":"alerts_type_name",
                   #"order_by":"date_added",
                   "where[1]":"priority = (2)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[2]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def getMedAlertsByGroup(self,start,end,client,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"name",
                   "column[7]":"alerts_type_name",
                   #"order_by":"date_added",
                   "where[0]":"group_name = '%s'" % client,
                   "where[1]":"priority = (2)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[2]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def getHighAlerts(self,start,end,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"resource_name",
                   "column[7]":"alerts_type_name",
                   #"order_by":"date_added",
                   "where[1]":"priority = (1)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[2]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def getHighAlertsByGroup(self,start,end,client,lm=0,ct=""):
          ndata = {"column[0]":"date_added",
                   "column[1]":"ip_src",
                   "column[2]":"ip_dst",
                   "column[3]":"ip_dport",
                   "column[4]":"ip_sport",
                   "column[5]":"alert_name",
                   "column[6]":"resource_name",
                   "column[7]":"alerts_type_name",
                   #"order_by":"date_added",
                   "where[0]":"group_name = '%s'" % client,
                   "where[1]":"priority = (1)",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          if lm != 0:
             ndata.update({"limit":"%s" % lm})
          if ct != "":
             ndata.update({"where[2]":"class_type = '%s'" % ct})
          return self.hawk.getEvents(ndata)

      def searchCIDRSrcByGroup(self,start,end,cidr,group,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "where[0]":'ip_src regex "%s")' % cidr,
                    "where[1]":"group_name = '%s'" % group,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchCIDRDstByGroup(self,start,end,cidr,group,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "where[0]":'ip_dst regex "/%s/"' % cidr,
                    "where[1]":"group_name = '%s'" % group,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)


      def searchIpSrc(self,start,end,ip,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "where[0]":"ip_src = ('%s')" % ip,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchIpSrcByGroup(self,start,end,ip,client,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "order_by":"date_added",
                    "where[0]":"group_name = '%s'" % client,
                    "where[1]":"ip_src = ('%s')" % ip,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchResAddrByGroup(self,start,end,ra,client,lm=0):
           ndata = {"column[0]":"resource_addr",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "column[10]":"payload",
                    #"order_by":"date_added",
                    "where[0]":"group_name = '%s'" % client,
                    "where[1]":"resource_addr = ('%s')" % ra,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
               ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchIpDst(self,start,end,ip,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "where[0]":"ip_dst = ('%s')" % ip,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchIpDstByGroup(self,start,end,ip,client,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "order_by":"date_added DESC",
                    "where[0]":"group_name = '%s'" % client,
                    "where[1]":"ip_dst = ('%s')" % ip,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchRes(self,start,end,res,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "column[10]":"resource_name",
                    "where[0]":"resource_name = ('%s')" % res,
                    "order_by":"date_added ASC",
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def searchResByGroup(self,start,end,res,group,lm=0):
           ndata = {"column[0]":"ip_src",
                    "column[1]":"ip_dst",
                    "column[2]":"alert_name",
                    "column[3]":"date_added",
                    "column[4]":"alerts_type_name",
                    "column[5]":"name",
                    "column[6]":"ip_dport",
                    "column[7]":"ip_sport",
                    "column[8]":"priority",
                    "column[9]":"group_name",
                    "column[10]":"resource_name",
                    "where[0]":"resource_name = ('%s')" % res,
                    "where[1]":"group_name = ('%s')" % group,
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           return self.hawk.getEvents(ndata)

      def getSuccessLoginsByGroup(self,start,end,client,ip="",lm=0,tp="action"):
           ndata = {"column[0]":"correlation_username",
                    "column[0]":"date_added",
                    "column[1]":"ip_src",
                    "column[2]":"alert_name",
                    "column[3]":"name",
                    "column[5]":"group_name",
                    "where[0]":"group_name = '%s'" % client, 
                    "where[1]":"correlation_username != ''",
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           if ip != "":
              ndata.update({"where[3]":"ip_src = '%s'" % ip})
           if tp == "login":
              ndata.update({"where[2]":"audit_login = ('success')"})
           elif tp == "action":
               ndata.update({"where[2]":"audit_user_action = ('success')"}) 
           return self.hawk.getEvents(ndata)

      def getFailedLoginsByGroup(self,start,end,client,ip="",lm=0,tp="login"):
           ndata = {"column[0]":"correlation_username",
                    "column[0]":"date_added",
                    "column[1]":"ip_src",
                    "column[2]":"alert_name",
                    "column[3]":"name",
                    "column[5]":"group_name",
                    "where[0]":"group_name = '%s'" % client, 
                    "where[1]":"correlation_username != ''",
                    "begin":"%s" % start,
                    "end":"%s" % end}
           if lm != 0:
              ndata.update({"limit":"%s" % lm})
           if ip != "":
              ndata.update({"where[3]":"ip_src = '%s'" % ip})
           if tp == "login":
              ndata.update({"where[2]":"audit_login = ('failure')"})
           elif tp == "action":
              ndata.update({"where[2]":"audit_user_action = ('failure')"})
           return self.hawk.getEvents(ndata)

      def getLogCount(self,start,end,client):
          ndata = {"column[0]":"resource_addr",
                   "column[1]":"group_name",
                   "column[2]":"count alert_name",
                   "where[0]":"group_name = '%s'" % client,
                   "order_by":"alert_name_count DESC",
                   "group_by":"resource_addr",
                   "begin":"%s" % start,
                   "end":"%s" % end}
          return self.hawk.getEvents(ndata)

      def getTopVulns(self,client,lm=10):
          ndata = {"column[0]":"vuln_name",
                   "column[1]":"count vuln_name",
                   "column[2]":"group_name",
                   "group_by":"vuln_name",
                   "order_by":"vuln_name_count DESC",
                   "where[0]":"group_name = ('%s')" % client,
                   "limit":"%s" % str(lm)}
          return self.hawk.getVulns(ndata)

      def getTopVulnSev(self,client,lm=10):
          ndata = {"column[0]":"severity",
                  "column[1]":"count severity",
                  "column[2]":"group_name",
                  "group_by":"severity",
                  "order_by":"severity_count DESC",
                  "where[0]":"group_name = ('%s')" % client,
                  "limit":"%s" % str(lm)}
          return self.hawk.getVulns(ndata)

      def getTopVulnHost(self,client,lm=10):
          ndata = {"column[0]":"resource_name",
                   "column[1]":"count resource_name",
                   "column[2]":"group_name",
                   "column[3]":"resource_address",
                   "group_by":"resource_name",
                   "order_by":"resource_name_count DESC",
                   "where[0]":"group_name = ('%s')" % client,
                   "limit":"%s" % str(lm)}
          return self.hawk.getVulns(ndata)

      def getTopVulnPort(self,client,lm=10):
          ndata = {"column[0]":"ip_port",
                   "column[1]":"count ip_port",
                   "column[2]":"group_name",
                   "group_by":"ip_port",
                   "order_by":"ip_port_count DESC",
                   "where[0]":"group_name = ('%s')" % client,
                   "where[1]":"ip_port != '0'",
                   "limit":"%s" % str(lm)}
          return self.hawk.checkData(self.hawk.getVulns(ndata))

      def getTimeDiffByGroup(self,client):
          ndata = {"column[0]":"resource_name",
                   "column[1]":"resource_address",
                   "column[4]":"resource_group",
                   "column[2]":"last_seen",
                   "column[5]":"class_type",
                   "column[3]":"timediff_seconds last_seen",
                   "group_by":"resource_name",
                   "where[0]":"resource_group = ('%s')" % client}
          return self.hawk.getDevices(ndata)
