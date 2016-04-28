#!/usr/bin/env	python
##--coding=utf-8--##
import urllib2
import urllib
import json
import sys
import datetime
import time
import os
import re
import socket
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')




def monitor_A(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)
        value_total=urljson["total"]
        if(value_total>0):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_B(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)

        minvalue_data=min(urljson["data"])

        if(minvalue_data>0):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_C(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)

        maxvalue_data=max(urljson["data"])

        if(maxvalue_data>0):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_D(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)

        datalist=urljson["data"]
        lendatalist=len(datalist)
        count_datalist=Counter(datalist)
        count_datalist0=count_datalist[0]

        if (count_datalist0+5<=lendatalist):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_E(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)

        urljsonlist_series=urljson["series"]
        maxdata_continentlist=[]
        for continentdict in urljsonlist_series:
            maxdata_continent=continentdict["data"]
            maxdata_continentlist.extend(maxdata_continent)

        if(maxdata_continentlist==[]):
            print 0
        else:
            print 1
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_F(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)
        value_ngroups=urljson["ngroups"]

        if(value_ngroups>0):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_G(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)
        value_datas=urljson["data"]
        maxvalue_data=max(value_datas)

        if(maxvalue_data>0):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


def monitor_H(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)
        value_total=urljson["total"]

        if(value_total>10):
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0

def monitor_I(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=10).read()
        urljson=json.loads(urldata)
        value_datas=urljson['data']
        value_usdata=value_datas[5]
        value_jpdata=value_datas[6]
        count_datalist=Counter(value_datas)
        count_data0=count_datalist[0]

        if value_jpdata>0 and value_usdata>0 and len(value_datas)-count_data0>=3:
            print 1
        else:
            print 0
    except socket.timeout, e:
        print 2
    except urllib2.URLError, e:
        print 0


if __name__ == '__main__':
    today=time.strftime('%Y%m%d',time.localtime(time.time()))
    today2=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    now=time.time()
    twoDaysBefore1=now-86400
    twoDaysBefore=time.strftime('%Y%m%d',time.localtime(twoDaysBefore1))
    oneWeekBefore1=now-604800
    oneWeekBefore=time.strftime('%Y%m%d',time.localtime(oneWeekBefore1))
    oneWeekBefore2=time.strftime('%Y-%m-%d',time.localtime(oneWeekBefore1))


    PROJECT_A = {         #接口url
    }

    PROJECT_B = {         #接口url
    }

    PROJECT_C = {         #接口url      
    }

    PROJECT_D = {         #接口url 
    }


    PROJECT_E = {         #接口url
    }

    PROJECT_F = {         #接口url         
    } 

    PROJECT_G = {         #接口url
    }

    PROJECT_H = {         #接口url
    }

    PROJECT_I = {         #接口url         
    }



    PROJECT=[PROJECT_A,PROJECT_B,PROJECT_C,PROJECT_D,PROJECT_E,PROJECT_F,PROJECT_G,PROJECT_H]
    PROJECT_NAMES_list=[]
    for i in range(0,len(PROJECT)):
        PROJECT_NAMES=PROJECT[i].keys()
        for j in range(0,len(PROJECT_NAMES)):
            PROJECT_NAMES_list.append(PROJECT_NAMES[j])
    DATA = {"data":[]}
    for n in PROJECT:
        DATA["data"] = [{"{#PROJECT_NAME}" : i} for i in PROJECT_NAMES_list ]


    if len(sys.argv) == 1 :
        print json.dumps(DATA,indent=4)
    elif sys.argv[1] in PROJECT_A.keys():
        url = PROJECT_A[sys.argv[1]]
        name =sys.argv[1]
        monitor_A(name,url)
    elif sys.argv[1] in PROJECT_B.keys():
        url = PROJECT_B[sys.argv[1]]
        name =sys.argv[1]
        monitor_B(name,url)
    elif sys.argv[1] in PROJECT_C.keys():
        url = PROJECT_C[sys.argv[1]]
        name =sys.argv[1]
        monitor_C(name,url)
    elif sys.argv[1] in PROJECT_D.keys():
        url = PROJECT_D[sys.argv[1]]
        name =sys.argv[1]
        monitor_D(name,url)
    elif sys.argv[1] in PROJECT_E.keys():
        url = PROJECT_E[sys.argv[1]]
        name =sys.argv[1]
        monitor_E(name,url)
    elif sys.argv[1] in PROJECT_F.keys():
        url = PROJECT_F[sys.argv[1]]
        name =sys.argv[1]
        monitor_F(name,url)
    elif sys.argv[1] in PROJECT_G.keys():
        url = PROJECT_G[sys.argv[1]]
        name =sys.argv[1]
        monitor_G(name,url)
    elif sys.argv[1] in PROJECT_H.keys():
        url = PROJECT_H[sys.argv[1]]
        name =sys.argv[1]
        monitor_H(name,url)
    elif sys.argv[1] in PROJECT_I.keys():
        url = PROJECT_I[sys.argv[1]]
        name =sys.argv[1]
        monitor_I(name,url)
