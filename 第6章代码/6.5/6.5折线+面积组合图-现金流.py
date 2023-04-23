from pyecharts import options as opts
from pyecharts.charts import Line
import pandas as pd
df=pd.read_excel(r'd:\图片\现金流量表.xlsx')    #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist()

x=[]
y1=[]
y2=[]
y3=[]

for data in df_list:
    x.append(data[0])
    y1.append(data[1])
    y2.append(data[2])
    y3.append('%.2f'%data[3])   

l= Line()

l.add_xaxis(x)
l.add_yaxis('现金流入', y1,color='#FF1493',is_smooth=True)   
l.add_yaxis('现金流出', y2,color='#00BFFF',is_smooth=True)     
l.add_yaxis('现金流净额', y3,color='#FFA500',areastyle_opts=opts.AreaStyleOpts(opacity=0.5),is_smooth=True,
            symbol='arrow',markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='min')]))

l.set_global_opts(title_opts=opts.TitleOpts('公司现金流分析',pos_left='5%'),
                  xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_align_with_label=True),is_scale=False,boundary_gap=False))
l.render(path='d:\\图片\\折线+面积组合图-现金流.html')   #注意：运行程序前请确保D盘有“图片”文件夹

