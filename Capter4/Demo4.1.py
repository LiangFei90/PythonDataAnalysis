# -*- coding: utf-8 -*-
#拉格朗日插值
import pandas as pd
from scipy.interpolate import lagrange

inputfile='C:\PythonDataAnalysisAndMining\Sources\chapter3\demo\data\catering_sale.xls'
outputfile='C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter4\output_files.xls'
data=pd.read_excel(inputfile)
data[u'销量'][(data[u'销量']<400)|(data[u'销量']>5000)]=None
print data
def ployinterp_column(s,n,k=5):
    if n>5:
        y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    elif n>len(s)-k:
        y=s[list(range(n-k,n))+list(range(n+1,len(s)))]
    else:
        y=s[list(range(0,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]
    #print y
    return lagrange(y.index,list(y))(n)
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j]=ployinterp_column(data[i],j)
            print("%s,%s,%s" %(i,j,data[i][j]))
data.to_excel(outputfile)
