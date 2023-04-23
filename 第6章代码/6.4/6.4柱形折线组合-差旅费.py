from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Grid
from pyecharts.globals import ThemeType
import pandas as pd
df=pd.read_excel(r'd:\图片\公司差旅费明细.xlsx')    #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist() 

x=[]
y1=[]
y2=[]
y3=[]
for data in df_list: 
    x.append(data[0])
    y1.append(data[1])
    y2.append(data[2])
    y3.append('%.2f'%(data[4]*100))

l=Line()
b= Bar()
g=Grid(init_opts=opts.InitOpts(theme = ThemeType.PURPLE_PASSION))
b.add_xaxis(x)
b.add_yaxis('标准金额', y1, category_gap='35%',z=0)
b.add_yaxis('实际报销金额', y2, category_gap='35%',z=0)
b.extend_axis(yaxis=opts.AxisOpts(type_='value', name='百分比',min_=0,max_=60,position='right',
                                  axislabel_opts=opts.LabelOpts(formatter='{value} %')))
b.set_global_opts(title_opts=opts.TitleOpts(title='公司差旅费分析',pos_left='3%'))

l.add_xaxis(x)
l.add_yaxis("超出占比",y3,yaxis_index = 1)

b.overlap(l)

g.add(chart = b,grid_opts = opts.GridOpts(),is_control_axis_index =True)
g.render(path='d:\\图片\\柱形折线组合图-差旅费.html')   #注意：运行程序前请确保D盘有“图片”文件夹

