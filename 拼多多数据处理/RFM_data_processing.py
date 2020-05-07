import numpy as np
import pandas as pd
import time

start=time.time()
#导入文件
df=pd.read_csv('./E-commerce order data.csv',encoding='gbk')
#打印数据，查看数据结构，是否有缺失
# print(df.head(1))
# print(df.info())
# df=pd.DataFrame(df,columns=['订单号','收货人','商品总价','区','订单确认时间']) 选择需要的数据赋值给新的数据框

#新建一列用来存放消费频率
df['ord_number']=pd.DataFrame(np.ones((df.shape[0],1)))
#将订单号设为索引列
df.set_index('订单号',inplace=True)

#存放索引和收货人
L = []

for i in df.index.tolist():
    if len(L) == 0:
        L.append([i, df.loc[i, '收货人']])
    else:
        for j in L:
            if df.loc[i,'收货人'] == j[1] and df.loc[i,'区'] == df.loc[j[0],'区']:
                df.loc[j[0],'ord_number'] = df.loc[j[0],'ord_number']+1  #将相同的顾客在消费频率上加1
                df.loc[j[0],'商品总价(元)'] = df.loc[j[0],'商品总价(元)'] + df.loc[i,'商品总价(元)'] #消费金额相加
                df.drop(i, inplace=True)  #删除重复项
                break
        else:
            #将不重复的数据的索引和收货人放入列表
            ord_info=[i,df.loc[i,'收货人']]
            L.append(ord_info)

# print(df.iloc[0])
new_data=pd.DataFrame(df,columns=['商品总价(元)','订单确认时间','ord_number'])
new_data.to_csv('Post-cleaning data.csv',header=True,index=True) #将数据写到csv文件中
end=time.time()
print(end-start)