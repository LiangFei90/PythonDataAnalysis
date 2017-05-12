# -*- coding: utf-8 -*-
#数据规范化
import pandas as pd

inputfile='C:\PythonDataAnalysisAndMining\Sources\chapter7\demo\data\\zscoredata.xls'
outputfile='C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter7\\aftercoredata.xls'

data=pd.read_excel(inputfile)
data=(data-data.mean(axis=0))/data.std(axis=0) #零-均值规范化
data.columns=['Z'+i for i in data.columns]
data.to_excel(outputfile)