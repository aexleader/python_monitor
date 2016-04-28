#coding=utf-8
import urllib2
import urllib
import socket
import json
import datetime
import time
import sys
import os  
import re 
reload(sys)
sys.setdefaultencoding('utf-8')
def fobj_listdata(name,url):
	#判断json中listdata的长度是否为空，为空就返回0，不为空就返回长度
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		global time1
		time1=time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
		lenth=len(urljson)
		if (lenth>0):
			return '%s:%s............%s' %(time1,name,lenth)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)

	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)
def fobj_totalzero(name,url):
	#判断total的值是否大于0，大于0就返回total的值，否则返回0
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		value=urljson['total']
		global time1
		time1=time.strftime("%Y-%m-%d %H:%M %p", time.localtime())
		if(value>0):
			return '%s:%s............%s' %(time1,name,value)
		else:
			return '%s:%s...........................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)

	
def fobj_count1(name,url):
	#判断obj_count的长度是否为0，为0就直接输出0，不为0就几点接口的value的值为0的个数是多少个，超过一半就报错
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		if (len(urljson['obj_count'])>0):
			count=0
			for i in xrange(0,len(urljson['obj_count'])-1):
				bb=urljson["obj_count"][i]['value']
				if (bb==u'0'):
					count+=1	
			return '%s:%s............%s' %(time1,name,count) 			
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)

	
# 	# print "count = ", count
def fobj__count2(name,url):
	#判断obj_count的长度是否为0，为0就直接输出0，不为0就几点接口的value的值为0的个数是多少个，超过一半就报错
	try:
		urlContent=urllib2.urlopen(url).read()
		urljson=json.loads(urlContent)
		if (len(urljson['obj_count'])>0):	
			count=0
			for i in xrange(0,len(urljson['obj_count'])-1):
				bb=urljson["obj_count"][i]['value']
			# print "bb= ", bb ,type(bb)
				if (bb==u'0'):
					count+=1
			return '%s:%s............%s' %(time1,name,count) 
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)
def fobj__count4(name,url):
	try:
		#判断obj_count的长度是否为0，为0就直接输出0，不为0就几点接口的value的值为0的个数是多少个，超过一半就报错
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		if (len(urljson['obj_count'])>0):	
			count=0
			for i in xrange(0,len(urljson['obj_count'])-1):
				bb=urljson["obj_count"][i]['value']
			# print "bb= ", bb ,type(bb)
				if (bb==u'0'):
					count+=1	
			return '%s:%s............%s' %(time1,name,count)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)

def fobj__ngroups(name,url):
	try:
		#判断ngroups的值是否大于0，如果大于0就直接输出ngroups的值，否则返回0
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		#print urljson
		value=urljson['ngroups']
		if(value>0):
			return '%s:%s............%s' %(time1,name,value)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s............................................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s......................................................................Http request error' %(time1,name)

def fobj__categories(name,url):
	#先判断categories的值是否为空，如果不为空，再判断每个data的最小值是否大于0，返回每一个最小值，否则返回0，时间参数案例的起止时间
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		valuelen=len(urljson['categories'])

		if(valuelen>0):
			aalist=[]
			for i in xrange(0,5):
				datavalue=urljson['data'][i]['data']
				mindatavalue=min(datavalue)
				aalist.append(mindatavalue)
			#回头看看
			# print aalist
			minaalist=min(aalist)
			if(minaalist>0):
				return '%s:%s............%s' %(time1,name,minaalist)
			else:
				return '%s:%s.................................................Interface no data return' %(time1,name)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)	
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)
def fobj__list(name,url):
#判断list返回的是否为空,站点文章
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		urljsonlen=len(urljson)
		if(urljsonlen>0):
			return '%s:%s............%s' %(time1,name,urljsonlen)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回3
		return '%s:%s.......................................................Http request error' %(time1,name)
def fobj__totalrows(name,url):
#totalrows的值是否大于0，时间参数为当天
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		value=urljson[0]['totalrows']
		if(value>0):
			return '%s:%s............%s' %(time1,name,value)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回3
		return '%s:%s.......................................................Http request error' %(time1,name)

def fobj__response(name,url):
# 先判断response列表的长度是否为空，如果不为空就取numFound的值，为空，直接报错，时间参数为当天的数据
	try:
		urlContent=urllib2.urlopen(url,timeout=5).read()
		urljson=json.loads(urlContent)
		value=urljson['response']['numFound']
		if(len(urljson['response'])>0):
			return '%s:%s............%s' %(time1,name,value)
		else:
			return '%s:%s.................................................Interface no data return' %(time1,name)
	except socket.timeout, e:
		return '%s:%s......................................................request timeout' %(time1,name)
######5秒没有返回结果返回2
	except urllib2.URLError,e:
######404 501错误返回0
		return '%s:%s.......................................................Http request error' %(time1,name)

if __name__ == '__main__':  
	today=time.strftime('%Y%m%d',time.localtime(time.time()))
	now=time.time()
	twoDaysBefore1=now-172800
	twoDaysBefore=time.strftime('%Y%m%d',time.localtime(twoDaysBefore1))
	SixDaysBefore1=now-518400
	SixDaysBefore=time.strftime('%Y%m%d',time.localtime(SixDaysBefore1))
	sixhoursBefore1=now-18000
	sixhoursBefore=time.strftime('%Y%m%d',time.localtime(sixhoursBefore1))
	#今天日期包括时分
	todaydate=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
	now=time.time()
	sixhoursBefore1=now-21600
	sixhoursBeforedate=time.strftime('%Y%m%d%H%M',time.localtime(sixhoursBefore1))
	threehoursBefore3=now-10800
	threehoursBeforedate=time.strftime('%Y%m%d%H%M',time.localtime(threehoursBefore3))

#listData的长度不为空，为空则告警，值保留三天的，所以只取前两天
listdata={         #url
}

#total的值不为0，时间参数为当天

totalzero={        #url
}

#obj_count的长度不为0，
obj_count1={       #url
}
#obj_count的长度不为0，时间为前一个取一周的数据,后两个取当天的数据
obj_count2={       #url
}
# obj_count的长度是否为0，时间参数为当天的时间
obj_count4={       #url
}
# ngroups的值是否为0，
ngroups={          #url
}
#先判断categories的值是否为空，如果不为空，再判断每个data的最小值是否大于0，时间参数案例的起止时间
categories={       #url
}

# 判断list返回的是否为空,站点文章,时间为案例的起止时间
list={             #url
}
#totalrows的值是否大于0，时间参数为案例的起止
obj_totalrows={    #url
}
# 先判断response列表的长度是否为空，如果不为空就取numFound的值，为空，直接报错，时间参数为当天的数据
response={         #url
}
for name in listdata:
    ldvalue=fobj_listdata(name,listdata[name])
    files = open('e:\\test2.html','a')
    files.write(ldvalue)
    files.write('<br>')
    files.write('\n')
    files.close()
for name in totalzero:
	tzvalue=fobj_totalzero(name,totalzero[name])
	files = open('e:\\test2.html','a')
	files.write(tzvalue)
	files.write('<br>')
	files.write('\n')
	files.close()
files = open('e:\\test2.html','a')
for name in obj_count1:
	bbcount1=fobj_count1(name,obj_count1[name])	
	bbcount1_re=re.search('\d+$',bbcount1)
	# print bbcount1_re.group()
	cc=bbcount1_re.group()
	icc=int(cc)
	
	files.write(bbcount1)
	if(icc > 24):
		nn='大于一半地区的数据为0'
		files.write('............'+nn)
		files.write('<br>')
	else:
		ff='zc'
		files.write('..............'+ff)
		files.write('<br>')
files.close()
files = open('e:\\test2.html','a')
for name in obj_count2:
	bbcount2=fobj__count2(name,obj_count2[name])
	bbcount1_re=re.search('\d+$',bbcount1)
	# print bbcount1_re.group()
	cc=bbcount1_re.group()
	icc=int(cc)
	files.write(bbcount2)
	if(icc>17):
		gg='大于一半地区的数据为0'
		files.write('............'+gg)
		files.write('<br>')
	else:
		fg='zc'
		files.write('..............'+fg)
		files.write('<br>')
files.close()
files = open('e:\\test2.html','a')
for name in obj_count4:
	bbcount4=fobj__count4(name,obj_count4[name])
	bbcount4_re=re.search('\d+$',bbcount1)
	# print bbcount1_re.group()
	cc=bbcount4_re.group()
	icc=int(cc)
	files.write(bbcount4)
	if(icc> 6 ):
		nn='大于一半地区的数据为0'
		files.write('............'+nn+'<br>')
		# files.write('<br>')
	else:
		ff='zc'
		files.write('..............'+ff+'<br>')
		# files.write('<br>')
files.close()		
for name in ngroups:
	bbngroups=fobj__ngroups(name,ngroups[name])
	files = open('e:\\test2.html','a')
	files.write(bbngroups)
	files.write('<br>')
	files.write('\n')
	files.close()
for name in list:
	bblist=fobj__list(name,list[name])
	files = open('e:\\test2.html','a')
	files.write(bblist)
	files.write('<br>')
	files.write('\n')
	files.close()
for name in categories:
	bbcategories=fobj__categories(name,categories[name])
	files = open('e:\\test2.html','a')
	files.write(bbcategories)
	files.write('<br>')
	files.write('\n')
	files.close()

for name in obj_totalrows:
	bbobjtotalrows=fobj__totalrows(name,obj_totalrows[name])
	files = open('e:\\test2.html','a')
	files.write(str(bbobjtotalrows))
	files.write('<br>')
	files.write('\n')
	files.close()

for name in response:
	bbresponse=fobj__response(name,response[name])
	files = open('e:\\test2.html','a')
	files.write(bbresponse)
	files.write('<br>')
	files.write('\n')
	files.close()
f=open('d:\\test2.html','a+')
f.write('======================')
f.write('<br>')
f.close()
