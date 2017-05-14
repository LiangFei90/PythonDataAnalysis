#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:34:00 2017

@author: frank
"""
#from __future__ import print_function
import time

import pandas as pd
from sklearn.cluster import KMeans

inputfile='/home/frank/PythonDataAnalysisAndMining/Sources/chapter8/demo/data/data.xls'
outputfile='/home/frank/PythonDataAnalysis/data_processde.xls'

typelabel={u'肝气郁结证型系数':'A',u'热毒蕴结证型系数':'B',
           u'冲任失调证型系数':'C',u'气血两虚证型系数':'D',
           u'脾胃虚弱证型系数':'E',u'肝肾阴虚证型系数':'F'}
k=4

data=pd.read_excel(inputfile)

keys=list(typelabel.keys())

result=pd.DataFrame()

def transform(result,data,keys):
    form=data.copy()
    for i in range(len(keys)):       
        print (u'正在转换第%d列' %(i+1))
        start=time.clock()
        for j in range(0,len(data[[i]])):  
        #for j in range(0,20): 
            for n in range(1,4):                             
                if result.ix[2*i,n]<form.ix[j,i]<result.ix[2*i,n+1] or form.ix[j,i]==0:
                    #print data.ix[j,i]
                    form.ix[j,i]=result.index[2*i]+str(n)
                    break
                    #print data.ix[j,i]
                elif n==3 and result.ix[2*i,n+1]<form.ix[j,i]:                  
                    form.ix[j,i]=result.index[2*i]+'4' 
                    #print('It is D :%d,%d,%s' % (j,i,form.ix[j,i]))
                    
                
        end=time.clock()
        print (u'用时：%.2f s' %(end-start))
    form.to_excel('/home/frank/PythonDataAnalysis/aftertrans.xls')

if __name__ =='__main__':
    
    for i in range(len(keys)):
        print(u'正在进行 "%s" 的聚类...' % keys[i])
        kmodel=KMeans(n_clusters=k,n_jobs=1)
        kmodel.fit(data[[i]].as_matrix())#as_matrix zhuancheng juzheng
        r1=pd.DataFrame(kmodel.cluster_centers_,columns=[typelabel[keys[i]]])
        r2=pd.Series(kmodel.labels_).value_counts()
        r2=pd.DataFrame(r2,columns=[typelabel[keys[i]]+'n'])
        r=pd.concat([r1,r2],axis=1).sort(typelabel[keys[i]])       
        r.index=[1,2,3,4]
        
        r[typelabel[keys[i]]]=pd.rolling_mean(r[typelabel[keys[i]]],2)#rolling_mean() 用来计算相邻2列到均值，以此作为边界
        r[typelabel[keys[i]]][1]=0.0 #这两句将原来到聚类中心改为边界点
  
        result=result.append(r.T)
    result=result.sort()
    
    print result
    transform(result,data,keys)
    #result.to_excel(outputfile)