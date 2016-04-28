#!/usr/bin/env	python
##--coding=utf-8--##
import sys
import json
import pymssql
import time

def get_data(name):
    try:
        conn = pymssql.connect(host="host", user="user", password="pwd", database="databasename", charset='utf8', port='port', as_dict=False)
        cursor = conn.cursor()
        cursor.execute(name)
        results = cursor.fetchall()
        conn.close()
        return results
    except pymssql.OperationalError, msg:
        return 2

def res():
    res=get_data(sql)
    if res==[]:
        print 0     #判断条件：该服务器记录中的LastTime >= （当前时间-30分钟），如果取得结果为空，则返回0
    elif res==2:
        print 2     #如果连不上数据库则返回2
    else:
        print 1     #如果连上数据库后返回结果不为空，说明正常，返回1


if __name__ == '__main__':
    ALL_PROJECT = {
"#服务器名称":    "select * from [Winxin].[dbo].[Heartbeat] where Remoteconnection='#服务器名称' and Datediff(mi,LastTime,GetDate())<30",
}    #用sql语句从服务器获取数据，LastTime >= （当前时间-30分钟）
    ALL_DATA = {"data":[]}
    ALL_DATA["data"] = [{"{#server_ip:port}" : i} for i in ALL_PROJECT.keys()]
    if len(sys.argv) == 1 :
        print json.dumps(ALL_DATA,indent=4)
    elif sys.argv[1] in ALL_PROJECT.keys():
        sql = ALL_PROJECT[sys.argv[1]]
        res()
