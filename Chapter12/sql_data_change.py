#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:28:05 2017

@author: frank
"""
import pandas as pd
from sqlalchemy import create_engine


engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/WebAn?charset=utf8')
sql=pd.read_sql('cleaned_gzdata',engine,chunksize=2500)

for l in sql:
    d=l.copy()
    d['fullURL']=d['fullURL'].str.replace('_\d{0,2}.html','.html')
    
    d=d.drop_duplicates()#删除重复记录
    
    d.to_sql('changed_gzdata',engine,index=False,if_exists='append')