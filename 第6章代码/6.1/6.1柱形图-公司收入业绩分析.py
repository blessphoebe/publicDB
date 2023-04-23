from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd
#from pyecharts.globals import ThemeType
df=pd.read_excel(r'd:\图片\公司收入业绩分析.xlsx')    #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist()

x=[]
y1=[]
y2=[]
y3=[]
y4=[]
for data in df_list:
    x.append(data[0])
    y1.append(data[1])
    y2.append(data[2])
    y3.append(data[3])
    y4.append(data[4])

b= Bar()
b.add_xaxis(x)
b.add_yaxis('一季度', y1,color='#FFA500',category_gap='35%')   #紫
b.add_yaxis('二季度', y2,color='#00FFFF',category_gap='35%')     #粉
b.add_yaxis('三季度', y3,color='#FFB6C1',category_gap='35%')     #绿
b.add_yaxis('四季度', y4,color='#9932CC',category_gap='35%')     #橙色
#b.theme = ThemeType.PURPLE_PASSION
b.set_global_opts(title_opts=opts.TitleOpts('公司收入业绩分析',pos_left='5%'))
b.render(path='d:\\图片\\柱形图-公司收入业绩分析.html')     #注意：运行程序前请确保D盘有“图片”文件夹

