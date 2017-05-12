# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from sklearn.manifold import TSNE
#
#inputfile='~/PythonDataAnalysisAndMining/Sources/chapter7/demo/data/zscoredata.xls'
#k=5
#
#data=pd.read_excel(inputfile)
#
#kmodel=KMeans(n_clusters=k,n_jobs=1)# k为需要进行聚类的类别个数
#kmodel.fit(data)#训练模型
#
#
#r1=pd.Series(kmodel.labels_).value_counts()#统计各个类别的数目
#r2=pd.DataFrame(kmodel.cluster_centers_)#找出聚类中心
#r=pd.concat([r2,r1],axis=1)#横向连接（0是纵向连接），得到聚类中心对应的类别下的数目
#
#r.columns=data.columns.union(['leibie'])#添加列名‘类比数目’
##print r
#r_1=pd.concat([data,pd.Series(kmodel.labels_,index=data.index)],axis=1)
#r_1.columns=data.columns|['leibie']
##r_1.to_excel('C:\Users\LiangFei\Desktop\PythonDataAnalysis\Capter7\\aftercluster.xls')
#print r_1
data_z=pd.read_excel('/home/frank/PythonDataAnalysis/Capter7/test01.xlsx')
tsne=TSNE()
#print data_z
tsne.fit_transform(data_z)
tsne=pd.DataFrame(tsne.embedding_,index=data_z.index)
plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['asex.unicode_minus']=False
d=tsne[data_z['leibie']==0]
plt.plot(d[0],d[1],'r.')
d=tsne[data_z['leibie']==1]
plt.plot(d[0],d[1],'go')
d=tsne[data_z['leibie']==2]
plt.plot(d[0],d[1],'b*')
d=tsne[data_z['leibie']==3]
plt.plot(d[0],d[1],'m+')
d=tsne[data_z['leibie']==4]
plt.plot(d[0],d[1],'k^')
plt.show()