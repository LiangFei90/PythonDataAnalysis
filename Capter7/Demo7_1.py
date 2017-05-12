# -*- coding: utf-8 -*-
#对数据进行基本探索，
#返回空值数，最大值，最小值
#descripbe()会自动计算非空值count,唯一值数unique,频数最高top,最高频数freq,平均数mean,标准差std,
#最小值min,最大值max,中位数50%
import pandas as pd

inputfile='C:\PythonDataAnalysisAndMining\Sources\chapter7\demo\data\\air_data.csv'
outputfile='C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter7\explore.xls'
data=pd.read_csv(inputfile,encoding='utf-8')
explore=data.describe().T#T是转置，转置后更方便查阅
print explore['std']

#print len(data)
#print explore['count']
explore['null']=len(data)-explore['count']#计算空值的数量
#print type(explore)
explore=explore[['null','max','min']]
explore.columns=[u'空值数',u'最大值',u'最小值']
#print explore
explore.to_excel(outputfile)

