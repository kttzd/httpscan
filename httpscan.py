#!/usr/bin/python
# -*- coding: utf-8 -*-
#多端口请求http
__author__ = 'kttzd'


import sys
import httplib2



headers={}
headers['User-Agent']="Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"
#headers['Referer']=""  #如果需要Referer从这里面加上




address=sys.argv[1]

ports=map(str,range(80,3000)) #默认80-2999 自己修改




class httpscan():
    def __init__(self,address,ports,headers):
        self.address=address
        self.ports=ports
        self.headers=headers
    def scan(self):
        h=httplib2.Http(timeout=2) #默认timeout=2 自己修改
        try:
            for port in self.ports:
                host="http://"+self.address+":"+port
                print host
                try:
                    res,con=h.request(host,"HEAD",headers=self.headers)
                    print host+"----------------------------I GET IT"
                except Exception,e:
                    #print e #错误信息
                    pass
        except KeyboardInterrupt:
            print "Scan done\n"
        finally:
            print "Have a nice day"
if __name__=="__main__":
    test=httpscan(address,ports,headers)
    test.scan()
                
                
