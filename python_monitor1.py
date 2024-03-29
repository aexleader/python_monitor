#coding=utf-8
import urllib2
import urllib
import json
import sys
import datetime
import time
import os
import re
import socket
reload(sys)
sys.setdefaultencoding('utf-8')


def monitor_a(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        urljson_values=list(urljson.values())
        minvalue=urljson_values[urljson_values.index(min(urljson_values))]
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(minvalue>0):
            return '%s:%s..........%s'%(time1,name,minvalue)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
today=time.strftime('%Y%m%d',time.localtime(time.time()))
print monitor_a('NAME','URL')#NAME:接口名称,URL:接口地址
print monitor_a('NAME','URL(TIME1,TIME2)'.format(today,today))#NAME:接口名称，URL(TIME1,TIME2):接口地址


def monitor_b(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        minvalue=min(int(urldict["count"]) for urldict in urljson)
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(minvalue>0):
            return '%s:%s..........%s'%(time1,name,minvalue)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_b('NAME','URL')


def monitor_c(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        value_totalRows=urljson.get("totalRows")
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(value_totalRows>0):
            return '%s:%s..........%s'%(time1,name,value_totalRows)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_c('NAME','URL')


def monitor_d(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        minvalue=min(int(urldict["count"]) for urldict in urljson)#所有的count中值最小的不为0
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(minvalue>0):
            return '%s:%s..........%s'%(time1,name,minvalue)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_d('NAME','URL')


def monitor_e(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        minvalue=min(int(urldict["count"]) for urldict in urljson)#所有的count中，min(count)>0
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())

        if(minvalue>0):
            return '%s:%s..........%s'%(time1,name,minvalue)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_e('NAME','URL')


def monitor_f(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        value_day7=urljson[0]["weekStat"][3]["day7"]
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(value_day7>0):
            return '%s:%s..........%s'%(time1,name,value_day7)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_f('NAME','URL')


def monitor_g(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        value_countlist=[]
        for i in range(0,len(urljson)-1):
            value_count=int(urljson[i]["count"])
            value_countlist.append(value_count)
        urllist_weekStat=urljson[0]["weekStat"]
        for i in urllist_weekStat:
            if i["name"]=="北京":
                value_day7=i["day7"]
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(value_day7>0):
            return '%s:%s..........%s'%(time1,name,value_day7)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_g('NAME','URL')


def monitor_i(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        lenth=len(urljson)         #lenth大于0
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(lenth>0):
            return '%s:%s..........%s'%(time1,name,lenth)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_i('NAME','URL')


def monitor_j(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)

        value_total=urljson["total"]         #total>0，
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())

        if(value_total>0):
            return '%s:%s..........%s'%(time1,name,value_total)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
today=time.strftime('%Y%m%d',time.localtime(time.time()))
now=time.time()
twoWeeksBefore1=now-1209600
twoWeeksBefore=time.strftime('%Y%m%d',time.localtime(twoWeeksBefore1))
oneWeekBefore1=now-604800
oneWeekBefore=time.strftime('%Y%m%d',time.localtime(oneWeekBefore1))
oneMonthBefore1=now-2592000
oneMonthBefore=time.strftime('%Y%m%d',time.localtime(oneMonthBefore1))
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')
print monitor_j('NAME','URL')


def monitor_k(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        value_count=urljson["array"][0]["count"]         
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(value_count>0):
            return '%s:%s..........%s'%(time1,name,value_count)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_k('NAME','URL')


def monitor_h(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        day10=urljson[0]["weekStat"][0]["day1"]
        day20=urljson[0]["weekStat"][0]["day2"]
        day30=urljson[0]["weekStat"][0]["day3"]
        day40=urljson[0]["weekStat"][0]["day4"]
        day50=urljson[0]["weekStat"][0]["day5"]
        day60=urljson[0]["weekStat"][0]["day6"]
        day70=urljson[0]["weekStat"][0]["day7"]
        day11=urljson[0]["weekStat"][1]["day1"]
        day21=urljson[0]["weekStat"][1]["day2"]
        day31=urljson[0]["weekStat"][1]["day3"]
        day41=urljson[0]["weekStat"][1]["day4"]
        day51=urljson[0]["weekStat"][1]["day5"]
        day61=urljson[0]["weekStat"][1]["day6"]
        day71=urljson[0]["weekStat"][1]["day7"]
        value_daylist=[day10,day20,day30,day40,day50,day60,day70,day11,day21,day31,day41,day51,day61,day71]
        minvalue_day=min(value_daylist)
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(minvalue_day>0):
            return '%s:%s..........%s'%(time1,name,minvalue_day)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_h('NAME','URL')


def monitor_l(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        url_serieslist=urljson["series"]
        value_datalist=[]
        for i in range(0,len(url_serieslist)-1):
            value_data=int(urljson["series"][i]["data"][0])
            value_datalist.append(value_data)
        minvalue_data=min(value_datalist)
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(minvalue_data>0):
            return '%s:%s..........%s'%(time1,name,minvalue_data)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
today=time.strftime('%Y%m%d',time.localtime(time.time()))
print monitor_l('NAME','URL')


def monitor_m(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        url_serieslist=urljson["series"]
        value_datalist=[]
        for i in range(0,len(url_serieslist)-1):
            value_data=int(urljson["series"][i]["data"][0])
            value_datalist.append(value_data)
        maxvalue_data=max(value_datalist)
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(maxvalue_data>0):
            return '%s:%s..........%s'%(time1,name,maxvalue_data)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_m('NAME','URL')


def monitor_n(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        value_countlist=[]
        for i in range(0,len(urljson)-1):
            value_count=int(urljson[i]["count"])
            value_countlist.append(value_count)
        value1_count=value_countlist[0]
        value2_count=value_countlist[1]
        value3_count=value_countlist[2]
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())
        if(value1_count>0 and value2_count>0 and value3_count>0):
            return '%s:%s..........%s'%(time1,name,value1_count)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_n('NAME','URL')


def monitor_o(name,url):
    try:
        urldata=urllib2.urlopen(url,timeout=5).read()
        urljson=json.loads(urldata)
        for i in urljson:
            if i["name"]=="北京":
                value_count_beijing=i["count"]
        global time1
        time1=time.strftime("%Y-%m-%d %H:%M %p",time.localtime())

        if(value_count_beijing>0):
            return '%s:%s..........%s'%(time1,name,value_count_beijing)
        else:
            return '%s..........interface no data return'%name
    except socket.timeout, e:
        return '%s..........request time out'%name
    except urllib2.URLError, e:
        return '%s..........Http request error'%name
print monitor_o('NAME','URL')
















