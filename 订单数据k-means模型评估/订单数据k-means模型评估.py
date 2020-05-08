from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#导入k-means聚类后的文件
data=pd.read_csv('./K-MEANS聚类.csv',encoding='gbk')
# print(data.head())

# 打印查看数据类型
data.dtypes
# print(data)

# 找到列名，转化为列表
col = list(data[['消费金额','QCL_1']])

# 把所有列的类型都转化为数值型，出错的地方填入NaN，再把NaN的地方补删除
data[col] = data[col].apply(pd.to_numeric, errors='coerce')
data=data.dropna()

# 把需要转化类型的列都转化成float类型
data[['支付方式','QCL_1']]=data[['支付方式','QCL_1']].astype('float')

# 评判聚类效果，轮廓系数
silhouette_score(data.loc[:,['消费金额','消费频率','支付方式','订购周期']],data.loc[:,'QCL_1'])