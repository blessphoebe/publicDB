from pyecharts import options as opts
from pyecharts.charts import Bar,Line,Grid
#from pyecharts.globals import ThemeType
import pandas as pd
df=pd.read_excel(r'd:\图片\销售回款明细.xlsx')   #注意：运行前先将数据文件复制到D盘“图片”文件夹中
df_list = df.values.tolist()

x=[]
y1=[]
y2=[]
y3=[]
for data in df_list:
    
    x.append(data[1])
    y1.append(data[2])
    y2.append(data[3])
    y3.append('%.2f'%(data[4]*100))

l=Line()
b= Bar()
g=Grid()
b.add_xaxis(x)
b.add_yaxis('合同金额', y1,color='#2F4F4F', category_gap='35%',z=0)
b.add_yaxis('回款金额', y2,color='#DC143C', category_gap='35%',z=0)
b.extend_axis(yaxis=opts.AxisOpts(type_='value', name='百分比',min_=0,max_=100,position='right',
                                  axislabel_opts=opts.LabelOpts(formatter='{value} %')))
b.set_global_opts(title_opts=opts.TitleOpts(title='销售回款分析',pos_left='20%'))

#g.theme = ThemeType.PURPLE_PASSION
l.add_xaxis(x)
l.add_yaxis('回款率',y3,yaxis_index = 1,symbol='circle',linestyle_opts=opts.LineStyleOpts(color='cyan',width=1.5),
            label_opts=opts.LabelOpts(color='cyan'))



b.overlap(l)
g.add(chart = b,grid_opts = opts.GridOpts(),is_control_axis_index =True)


g.render(path='d:\\图片\\柱形图+折线.html')  #注意：运行程序前请确保D盘有“图片”文件夹

