#!/usr/bin/python
# -*- coding: utf-8 -*-
# 多端口请求http
# python httpscan.py example.com timeout port-from port-to (referer-url)
__author__ = 'kttzd'

import sys
import httplib2

headers={}
headers['User-Agent']="Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"

address=sys.argv[1]
times=int(sys.argv[2])
ports=map(str,range(int(sys.argv[3]),int(sys.argv[4])))
try:
    headers['Referer']=sys.argv[5]
except:
    pass

class httpscan():
    def __init__(self,address,ports,headers,times):
        self.address=address
        self.ports=ports
        self.headers=headers
        self.times=times
    def scan(self):
        h=httplib2.Http(timeout=self.times)
        try:
            for port in self.ports:
                host="http://"+self.address+":"+port
                print host
                try:
                    res,con=h.request(host,"HEAD",headers=self.headers)
                    print host+"-------------I GET IT"
                except Exception,e:
                    #print e
                    pass
        except KeyboardInterrupt:
            print "Scan done\n"
        finally:
            print "Have a nice day"

if __name__=="__main__":
    test=httpscan(address,ports,headers,times)
    test.scan()
