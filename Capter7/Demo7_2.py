# -*- coding: utf-8 -*-
#数据清理，去掉不符合规则的数据
import pandas as pd

inputfile='C:\PythonDataAnalysisAndMining\Sources\chapter7\demo\data\\air_data.csv'
outputfile='C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter7\data_cleaned.xls'
data=pd.read_csv(inputfile,encoding='utf-8')
data=data[data['EP_SUM_YR_1'].notnull()*data['EP_SUM_YR_2'].notnull()]
index1=data['EP_SUM_YR_1']!=0
index2=data['EP_SUM_YR_2']!=0
index3=(data['SEG_KM_SUM']==0)&(data['avg_discount']==0)
#保留票价不为0,或者里程和折扣同时为0 的数据
data=data[index1|index2|index3]

data.to_excel(outputfile)