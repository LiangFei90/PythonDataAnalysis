#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 18:39:45 2017

@author: frank
"""

import pandas as pd
from sqlalchemy import create_engine
from pymysql import connect

engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/WebAn?charset=utf8')
sql=pd.read_sql('all_gzdata',engine,chunksize=2500)
#conn=connect(host='localhost',port=3306,user='root',password='root',db='WebAn')
#cur=conn.cursor()
#lim1000=cur.execute("select * from all_gzdata limit 0,1000")
#table=cur.fetchmany(lim1000)
#for i in table:
#    print i[10]
counts=[i['fullURLId'].value_counts() for i in sql]#
counts=pd.concat(counts).groupby(level=0).sum()
#Level=0,按照第0级index分组，这里是指按照fullRULId进行分组，如果index(这里是fullURLId)相同，则合为一组
counts=counts.reset_index()
counts.columns=['index','num']
counts['type']=counts['index'].str.extract('(\d{3})')#提取前三个数字作为类别ID
counts_=counts[['type','num']].groupby('type').sum()
counts_['perscent']=counts_['num']/counts_['num'].sum()
counts_.sort('perscent',ascending=False)

#
#统计107类网页的情况
def count107(i):
    j=i[['fullURL']][i['fullURLId'].str.contains('107')].copy()
    j['type']=None
    j['type'][j['fullURL'].str.contains('info/.+?/')]=u'知识首页'
    j['type'][j['fullURL'].str.contains('info/.+?/.+?')]=u'知识列表页'
    j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')]=u'知识内容页'
    return j['type'].value_counts()

counts2=[count107(i) for i in sql]
counts2=pd.concat(counts2).groupby(level=0).sum()

c=[i['realIP'].value_counts() for i in sql]
counts3=pd.concat(c).groupby(level=0).sum()
counts3=pd.DataFrame(counts3)
counts3[1]=1
counts3.groupby(0).sum()



























    