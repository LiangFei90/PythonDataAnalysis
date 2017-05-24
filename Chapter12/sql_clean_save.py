#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:05:26 2017

@author: frank
"""

import pandas as pd
from sqlalchemy import create_engine

engine=create_engine('mysql+pymysql://root:root@127.0.0.1:3306/WebAn?charset=utf8')
sql=pd.read_sql('all_gzdata',engine,chunksize=2500)

for i in sql:
    d = i[['realIP','fullURL']]
    d=d[d['fullURL'].str.contains('.\html')].copy()
    
    d.to_sql('cleaned_gzdata',engine,index=False,if_exists='append')
    
